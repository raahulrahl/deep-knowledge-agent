"""deep-knowledge-agent - A Bindu Agent for deep research and knowledge exploration."""

import argparse
import asyncio
import json
import os
import sys
import traceback
from pathlib import Path
from textwrap import dedent
from typing import Any

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.models.openrouter import OpenRouter
from agno.tools.mem0 import Mem0Tools
from agno.vectordb.lancedb import LanceDb, SearchType
from bindu.penguin.bindufy import bindufy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Global agent instance
agent: Agent | None = None
_initialized = False
_init_lock = asyncio.Lock()


def load_config() -> dict:
    """Load agent configuration from project root."""
    # Try multiple possible locations for agent_config.json
    possible_paths = [
        Path(__file__).parent.parent / "agent_config.json",  # Project root
        Path(__file__).parent / "agent_config.json",  # Same directory as main.py
        Path.cwd() / "agent_config.json",  # Current working directory
    ]

    for config_path in possible_paths:
        if config_path.exists():
            try:
                with open(config_path) as f:
                    return json.load(f)
            except (PermissionError, json.JSONDecodeError) as e:
                print(f"⚠️  Error reading {config_path}: {type(e).__name__}")
                continue
            except Exception as e:
                print(f"⚠️  Unexpected error reading {config_path}: {type(e).__name__}")
                continue

    # If no config found or readable, create a minimal default
    print("⚠️  No agent_config.json found, using default configuration")
    return {
        "name": "deep-knowledge-agent",
        "description": "AI agent for deep knowledge exploration and research",
        "version": "1.0.0",
        "deployment": {
            "url": "http://127.0.0.1:3773",
            "expose": True,
            "protocol_version": "1.0.0",
            "proxy_urls": ["127.0.0.1"],
            "cors_origins": ["*"],
        },
        "environment_variables": [
            {"key": "OPENROUTER_API_KEY", "description": "OpenRouter API key for LLM calls", "required": True},
            {"key": "MEM0_API_KEY", "description": "Mem0 API key for memory operations", "required": True},
        ],
    }


def initialize_knowledge_base():
    """Initialize the knowledge base with your preferred documentation or knowledge source."""
    agent_knowledge = Knowledge(
        vector_db=LanceDb(
            uri="tmp/lancedb",
            table_name="deep_knowledge_knowledge",
            search_type=SearchType.hybrid,
            embedder=OpenAIEmbedder(id="text-embedding-3-small"),
        ),
    )
    # Add knowledge sources - user can customize this
    agent_knowledge.add_content(
        url="https://docs.agno.com/llms-full.txt",
    )
    return agent_knowledge


def get_agent_db():
    """Return agent storage."""
    return SqliteDb(session_table="deep_knowledge_sessions", db_file="tmp/agents.db")


async def initialize_agent() -> None:
    """Initialize the deep knowledge agent with proper model, tools, and knowledge base."""
    global agent

    # Get API keys from environment
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    mem0_api_key = os.getenv("MEM0_API_KEY")
    model_name = os.getenv("MODEL_NAME", "openai/gpt-4o")

    # Validate required API keys
    if not openrouter_api_key:
        error_msg = (
            "No OpenRouter API key provided. Set OPENROUTER_API_KEY environment variable.\n"
            "Get your key from: https://openrouter.ai/keys"
        )
        raise ValueError(error_msg)

    if not mem0_api_key:
        error_msg = (
            "No Mem0 API key provided. Set MEM0_API_KEY environment variable.\n"
            "Get your key from: https://app.mem0.ai/dashboard/api-keys"
        )
        raise ValueError(error_msg)

    # Initialize model
    model = OpenRouter(
        id=model_name,
        api_key=openrouter_api_key,
        cache_response=True,
        supports_native_structured_outputs=True,
    )
    print(f"✅ Using OpenRouter model: {model_name}")

    # Initialize knowledge base (optional)
    agent_knowledge = initialize_knowledge_base()

    # Initialize agent database (optional)
    agent_db = get_agent_db()

    # Initialize tools
    mem0_tools = Mem0Tools(api_key=mem0_api_key)

    # Create the deep knowledge agent
    agent = Agent(
        name="DeepKnowledge",
        model=model,
        tools=[mem0_tools],
        knowledge=agent_knowledge,
        db=agent_db,
        description=dedent("""\
            You are DeepKnowledge, an advanced reasoning agent designed to provide thorough,
            well-researched answers to any query by searching your knowledge base.

            Your strengths include:
            - Breaking down complex topics into manageable components
            - Connecting information across multiple domains
            - Providing nuanced, well-researched answers
            - Maintaining intellectual honesty and citing sources
            - Explaining complex concepts in clear, accessible terms"""),
        instructions=dedent("""\
            Your mission is to leave no stone unturned in your pursuit of the correct answer.

            To achieve this, follow these steps:
            1. **Analyze the input and break it down into key components**.
            2. **Search terms**: You must identify at least 3-5 key search terms to search for.
            3. **Initial Search:** Searching your knowledge base for relevant information. You must make at least 3 searches to get all relevant information.
            4. **Evaluation:** If the answer from the knowledge base is incomplete, ambiguous, or insufficient - Ask the user for clarification. Do not make informed guesses.
            5. **Iterative Process:**
                - Continue searching your knowledge base till you have a comprehensive answer.
                - Reevaluate the completeness of your answer after each search iteration.
                - Repeat the search process until you are confident that every aspect of the question is addressed.
            6. **Reasoning Documentation:** Clearly document your reasoning process:
                - Note when additional searches were triggered.
                - Indicate which pieces of information came from the knowledge base and where it was sourced from.
                - Explain how you reconciled any conflicting or ambiguous information.
            7. **Final Synthesis:** Only finalize and present your answer once you have verified it through multiple search passes.
                Include all pertinent details and provide proper references.
            8. **Continuous Improvement:** If new, relevant information emerges even after presenting your answer,
                be prepared to update or expand upon your response.

            **Communication Style:**
            - Use clear and concise language.
            - Organize your response with numbered steps, bullet points, or short paragraphs as needed.
            - Be transparent about your search process and cite your sources.
            - Ensure that your final answer is comprehensive and leaves no part of the query unaddressed.

            Remember: **Do not finalize your answer until every angle of the question has been explored.**"""),
        additional_context=dedent("""\
            You should only respond with the final answer and the reasoning process.
            No need to include irrelevant information.

            - Memory: You have access to your previous search results and reasoning process.
            """),
        add_history_to_context=True,
        num_history_runs=3,
        read_chat_history=True,
        add_datetime_to_context=True,
        markdown=True,
    )
    print("✅ Deep Knowledge Agent initialized")


async def run_agent(messages: list[dict[str, str]]) -> Any:
    """Run the agent with the given messages."""
    global agent
    if not agent:
        error_msg = "Agent not initialized"
        raise RuntimeError(error_msg)

    # Run the agent and get response
    response = await agent.arun(messages)
    return response


async def handler(messages: list[dict[str, str]]) -> Any:
    """Handle incoming agent messages with lazy initialization."""
    global _initialized

    # Lazy initialization on first call
    async with _init_lock:
        if not _initialized:
            print("🔧 Initializing Deep Knowledge Agent...")
            await initialize_agent()
            _initialized = True

    # Run the async agent
    result = await run_agent(messages)
    return result


async def cleanup() -> None:
    """Clean up any resources."""
    print("🧹 Cleaning up Deep Knowledge Agent resources...")
    # Clean up any resources if needed


def main():
    """Run the main entry point for the Deep Knowledge Agent."""
    parser = argparse.ArgumentParser(description="Bindu Deep Knowledge Agent")
    parser.add_argument(
        "--openrouter-api-key",
        type=str,
        default=os.getenv("OPENROUTER_API_KEY"),
        help="OpenRouter API key (env: OPENROUTER_API_KEY)",
    )
    parser.add_argument(
        "--mem0-api-key",
        type=str,
        default=os.getenv("MEM0_API_KEY"),
        help="Mem0 API key (env: MEM0_API_KEY)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=os.getenv("MODEL_NAME", "openai/gpt-4o"),
        help="Model ID for OpenRouter (env: MODEL_NAME)",
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Path to agent_config.json (optional)",
    )
    args = parser.parse_args()

    # Set environment variables if provided via CLI
    if args.openrouter_api_key:
        os.environ["OPENROUTER_API_KEY"] = args.openrouter_api_key
    if args.mem0_api_key:
        os.environ["MEM0_API_KEY"] = args.mem0_api_key
    if args.model:
        os.environ["MODEL_NAME"] = args.model

    print("🤖 Deep Knowledge Agent - Advanced Research Assistant")
    print("📚 Capabilities: Knowledge base search, iterative research, source citation")

    # Load configuration
    config = load_config()

    try:
        # Bindufy and start the agent server
        print("🚀 Starting Bindu Deep Knowledge Agent server...")
        print(f"🌐 Server will run on: {config.get('deployment', {}).get('url', 'http://127.0.0.1:3773')}")
        bindufy(config, handler)
    except KeyboardInterrupt:
        print("\n🛑 Deep Knowledge Agent stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
        traceback.print_exc()
        sys.exit(1)
    finally:
        # Cleanup on exit
        asyncio.run(cleanup())


if __name__ == "__main__":
    main()
