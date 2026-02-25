<p align="center">
  <img src="https://raw.githubusercontent.com/getbindu/create-bindu-agent/refs/heads/main/assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center">Deep Knowledge Agent</h1>
<h3 align="center">Advanced AI Research Assistant</h3>

<p align="center">
  <strong>In-depth analysis, knowledge synthesis, and comprehensive research on complex topics</strong><br/>
  Breaking down queries, validating facts, connecting insights, and delivering structured outputs
</p>

<p align="center">
  <a href="https://github.com/Paraschamoli/deep-knowledge-agent/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/Paraschamoli/deep-knowledge-agent/build-and-push.yml?branch=main" alt="Build Status">
  </a>
  <img src="https://img.shields.io/badge/python-3.12+-blue.svg" alt="Python Version">
  <a href="https://github.com/Paraschamoli/deep-knowledge-agent/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Paraschamoli/deep-knowledge-agent" alt="License">
  </a>
</p>

---

## Skills
The agent includes the `deep-knowledge` skill for comprehensive research capabilities:
- **Primary Capability**: Deep research and knowledge synthesis using iterative search and validation
- **Features**: Query decomposition into sub-topics, multi-source information aggregation, fact validation and cross-referencing, structured output generation
- **Limitations**: Requires reliable knowledge sources; processing time depends on query complexity

- **Secondary Capability**: Enhanced source integration and real-time updates (planned for v2.0.0)

---

## 🎯 What is Deep Knowledge Agent?

An AI-powered research assistant designed for deep, comprehensive analysis of complex topics. Think of it as having an expert researcher available 24/7 who doesn't just find answers, but understands them from multiple perspectives and synthesizes them into coherent, well-reasoned insights.

### Key Features
*   **🔍 Deep Research & Analysis** - Iterative search and validation across knowledge bases
*   **🧠 Knowledge Synthesis** - Connect insights across domains and disciplines
*   **✅ Fact Validation** - Cross-reference information from multiple reliable sources
*   **📊 Structured Output** - Well-organized reports with proper citations and reasoning
*   **⚡ Lazy Initialization** - Fast boot times, initializes on first request
*   **🔐 Secure API Handling** - No API keys required at startup

---

## 🛠️ Tools & Capabilities

### Core Technologies
*   **Knowledge Base Search** - Access and search comprehensive knowledge sources
*   **Mem0 AI Memory** - Persistent memory for context-aware research sessions
*   **Iterative Analysis** - Multi-pass research for thorough understanding
*   **Cross-Domain Synthesis** - Connect insights from different fields

### Research Methodology
1.  **Query Decomposition** - Break complex topics into manageable sub-topics
2.  **Iterative Search** - Multiple search passes to gather comprehensive information
3.  **Fact Validation** - Cross-reference and verify information across sources
4.  **Knowledge Synthesis** - Connect insights and identify patterns
5.  **Structured Reporting** - Deliver organized, well-reasoned outputs

---

> **🌐 Join the Internet of Agents**
> Register your agent at [bindus.directory](https://bindus.directory) to make it discoverable worldwide and enable agent-to-agent collaboration. It takes 2 minutes and unlocks the full potential of your agent.

---

## 🚀 Quick Start

### 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/Paraschamoli/deep-knowledge-agent.git
cd deep-knowledge-agent

# Set up virtual environment with uv
uv venv --python 3.12
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync
```

### 2. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your API keys:
OPENROUTER_API_KEY=your_openrouter_api_key_here
MEM0_API_KEY=your_mem0_api_key_here
```

### 3. Run Locally

```bash
# Start the deep knowledge agent
python -m deep_knowledge_agent

# Or using uv
uv run python -m deep_knowledge_agent
```

### 4. Test with Docker

```bash
# Build and run with Docker Compose
docker-compose up --build

# Access at: http://localhost:3773
```

---

## 🔧 Configuration

### Environment Variables
Create a `.env` file:

```env
# Required API Keys
OPENROUTER_API_KEY=your_openrouter_api_key_here  # Get from: https://openrouter.ai/keys
MEM0_API_KEY=your_mem0_api_key_here              # Get from: https://app.mem0.ai/dashboard/api-keys

# Optional
MODEL_NAME=openai/gpt-4o                         # OpenRouter model ID
DEBUG=true                                       # Enable debug logging
```

### Port Configuration
Default port: `3773` (can be changed in `agent_config.json`)

---

## 💡 Usage Examples

### Via JSON-RPC API

```bash
curl --location 'http://localhost:3773' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer sk-or-v1-...' \
--data '{
  "jsonrpc": "2.0",
  "method": "message/send",
  "params": {
    "message": {
      "role": "user",
      "parts": [
        {
          "kind": "text",
          "text": "Conduct a deep analysis of the competitive landscape for Notion, comparing it with ClickUp and Asana. Break the analysis into sub-topics including product capabilities, target market segments, pricing models, strengths, weaknesses, ecosystem integration, and long-term strategic positioning. Provide a structured and well-reasoned synthesis."
        }
      ],
      "kind": "message",
      "messageId": "770e8400-e29b-41d4-a716-446655440201",
      "contextId": "770e8400-e29b-41d4-a716-446655440202",
      "taskId": "770e8400-e29b-41d4-a716-446655440280"
    },
    "configuration": {
      "acceptedOutputModes": [
        "application/json"
      ]
    }
  },
  "id": "770e8400-e29b-41d4-a716-446655440204"
}'
```

### Sample Research Queries

```text
"Perform deep analysis on the ethical implications of AI in healthcare decision-making systems, considering bias, accountability, and patient autonomy."

"Investigate the relationship between climate change policies and economic growth in developing nations over the past decade, with specific case studies."

"Analyze the evolution of renewable energy technologies and their integration into national power grids, focusing on technical challenges and policy frameworks."

"Explore the intersection of neuroscience and artificial intelligence in understanding human cognition, including recent breakthroughs and future directions."
```

### Expected Output Format

```markdown
# [Comprehensive Research Title] 📚

## Executive Summary
Brief overview of key findings, scope, and significance...

## Research Methodology
- Query decomposition approach
- Search strategy and knowledge sources
- Validation methods employed

## Key Findings
1. Main discovery with supporting evidence
2. Statistical data and expert insights
3. Cross-domain connections identified
4. Patterns and trends observed

## Analysis & Insights
- Deep analysis of findings
- Contextual understanding
- Implications and consequences
- Stakeholder perspectives

## Knowledge Synthesis
- Connections across domains
- Integration of diverse insights
- Novel perspectives identified
- Framework development

## Sources & Validation
- List of primary sources with credibility assessment
- Cross-referencing methodology
- Confidence levels for key claims

## Further Research Directions
- Identified knowledge gaps
- Recommended investigation areas
- Emerging questions

---
Research conducted by Deep Knowledge Agent
Comprehensive Analysis Report
Date: {current_date}
Confidence Score: {0-1}
```

---

## 🐳 Docker Deployment

### Quick Docker Setup

```bash
# Build the image
docker build -t deep-knowledge-agent -f Dockerfile.agent .

# Run container
docker run -d \
  -p 3773:3773 \
  -e OPENROUTER_API_KEY=your_key_here \
  -e MEM0_API_KEY=your_mem0_key_here \
  --name deep-knowledge-agent \
  deep-knowledge-agent

# Check logs
docker logs -f deep-knowledge-agent
```

### Docker Compose (Recommended)

`docker-compose.yml`:

```yaml
version: '3.8'
services:
  deep-knowledge-agent:
    build:
      context: .
      dockerfile: Dockerfile.agent
    ports:
      - "3773:3773"
    environment:
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
      - MEM0_API_KEY=${MEM0_API_KEY}
    restart: unless-stopped
```

Run with Compose:

```bash
# Start with compose
docker-compose up -d

# View logs
docker-compose logs -f
```

---

## 📁 Project Structure

```text
deep-knowledge-agent/
├── deep_knowledge_agent/
│   ├── __init__.py              # Package initialization
│   ├── main.py                  # Main agent implementation
│   ├── agent_config.json        # Agent configuration
│   └── skills/
│       └── deep-knowledge/
│           └── skill.yaml       # Skill definition
├── pyproject.toml               # Python dependencies
├── Dockerfile.agent             # Docker build file
├── docker-compose.yml           # Docker Compose setup
├── README.md                    # This documentation
├── .env.example                 # Environment template
└── tests/                       # Test files
    └── test_main.py
```

---

## 🔌 API Reference

### Health Check

```bash
GET http://localhost:3773/health
```

Response:
```json
{"status": "healthy", "agent": "Deep Knowledge Agent"}
```

### Chat Endpoint

```bash
POST http://localhost:3773/chat
Content-Type: application/json

{
  "messages": [
    {"role": "user", "content": "Your research query here"}
  ]
}
```

For complete API documentation, visit: [Bindu API Reference](https://docs.getbindu.com)

---

## 🧪 Testing

### Local Testing

```bash
# Install test dependencies
uv sync --group dev

# Run tests
pytest tests/

# Test with specific API keys
OPENROUTER_API_KEY=test_key MEM0_API_KEY=test_key python -m pytest
```

### Integration Test

```bash
# Start agent
python -m deep_knowledge_agent &

# Test API endpoint
curl -X POST http://localhost:3773/chat \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Test research query"}]}'
```

---

## 🚨 Troubleshooting

### Common Issues & Solutions

**"ModuleNotFoundError"**
```bash
uv sync --force
```

**"Port 3773 already in use"**
Change port in `agent_config.json` or kill the process:
```bash
lsof -ti:3773 | xargs kill -9
```

**"No API key provided"**
Check if `.env` exists and variable names match. Or set directly:
```bash
export OPENROUTER_API_KEY=your_key
export MEM0_API_KEY=your_mem0_key
```

**Docker build fails**
```bash
docker system prune -a
docker-compose build --no-cache
```

**"OpenRouter API key required"**
Get a free key from OpenRouter or use their free models.

---

## 📊 Dependencies

### Core Packages
*   **bindu** - Agent deployment framework
*   **agno** - AI agent framework
*   **lancedb** - Vector database for knowledge storage
*   **tantivy** - Full-text search engine
*   **mem0ai** - Memory operations
*   **sqlalchemy** - Database ORM
*   **openai** - OpenAI client for embeddings
*   **python-dotenv** - Environment management

### Development Packages
*   **pytest** - Testing framework
*   **ruff** - Code formatting/linting
*   **pre-commit** - Git hooks

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1.  Fork the repository
2.  Create a feature branch: `git checkout -b feature/improvement`
3.  Make your changes following the code style
4.  Add tests for new functionality
5.  Commit with descriptive messages
6.  Push to your fork
7.  Open a Pull Request

**Code Style:**
*   Follow PEP 8 conventions
*   Use type hints where possible
*   Add docstrings for public functions
*   Keep functions focused and small

---

## 📄 License
MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Credits & Acknowledgments
*   **Developer:** Paras Chamoli
*   **Framework:** Bindu - Agent deployment platform
*   **Agent Framework:** Agno - AI agent toolkit
*   **Knowledge Base:** LanceDB with OpenAI embeddings
*   **Memory System:** Mem0 AI

## 🔗 Useful Links
*   🌐 **Bindu Directory:** [bindus.directory](https://bindus.directory)
*   📚 **Bindu Docs:** [docs.getbindu.com](https://docs.getbindu.com)
*   🐙 **GitHub:** [github.com/Paraschamoli/deep-knowledge-agent](https://github.com/Paraschamoli/deep-knowledge-agent)
*   💬 **Discord:** Bindu Community

<br>

<p align="center">
  <strong>Built with ❤️ by Paras Chamoli</strong><br/>
  <em>Advancing knowledge through AI-powered deep research</em>
</p>

<p align="center">
  <a href="https://github.com/Paraschamoli/deep-knowledge-agent/stargazers">⭐ Star on GitHub</a> •
  <a href="https://bindus.directory">🌐 Register on Bindu</a> •
  <a href="https://github.com/Paraschamoli/deep-knowledge-agent/issues">🐛 Report Issues</a>
</p>

> **Note:** This agent follows the Bindu pattern with lazy initialization and secure API key handling. It boots without API keys and only fails at runtime if keys are needed but not provided.
