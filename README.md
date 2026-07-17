# AgentOps Africa

Enterprise AI Executive Assistant Platform for African Businesses, Professionals, and SMEs

AgentOps Africa is an enterprise-grade AI assistant platform that combines Large Language Models (LLMs), Deep Research, workflow automation, and business intelligence to help professionals and organizations across Africa work more efficiently.

---

## ✨ Features

- 🤖 Deep Research Agents (DeepAgents)
- 💬 Multi-LLM Support
  - OpenAI
  - Google Gemini
  - Groq
  - OpenRouter
- 🔍 Investment & Company Research
- 📈 Financial Analysis
- 📧 Gmail Integration
- 📊 Google Sheets Integration
- ☁️ Google Drive Integration
- 💬 Telegram Assistant
- 🔗 MCP (Model Context Protocol) Support
- 🖥️ Streamlit Web Interface
- 🏢 Company Resolution & Intelligence
- 💹 Yahoo Finance Integration
- 🌍 Built for African Businesses

---

# Project Structure

```
agentops/
├── ai/                # AI clients and prompt templates
├── builders/          # Agent builders
├── clients/           # External API clients
├── config/            # Configuration
├── domains/
│   ├── companies/
│   ├── finance/
│   └── research/
├── providers/         # LLM & Finance providers
├── tools/             # LangChain tools
└── app.py
```

---

# Requirements

- Python 3.12+
- uv
- Git

---

# Installation

Clone the repository:

```bash
git clone <repository-url>

cd AgentOps-Africa
```

Install all dependencies:

```bash
uv sync
```

---

# Environment Variables

Create a `.env` file in the project root.

Example:

```env
LLM_PROVIDER=openai

OPENAI_API_KEY=your_key

TAVILY_API_KEY=your_key

GROQ_API_KEY=your_key

GOOGLE_API_KEY=your_key

OPENROUTER_API_KEY=your_key
```

---

# Running the Application

```bash
uv run python -m agentops.app
```

or

```bash
uv run streamlit run streamlit_app.py
```

(if using the Streamlit interface)

---

# Running Tests

```bash
uv run pytest
```

Run a specific test:

```bash
uv run pytest tests/test_research_engine_unit.py
```

---

# Linting

Check the project:

```bash
uv run ruff check .
```

Automatically fix issues:

```bash
uv run ruff check . --fix
```

Format the codebase:

```bash
uv run ruff format .
```

---

# Dependency Management

This project uses **uv**.

Install dependencies:

```bash
uv sync
```

Add a package:

```bash
uv add package-name
```

Add a development dependency:

```bash
uv add --dev package-name
```

Update dependencies:

```bash
uv lock --upgrade
```

---

# Supported LLM Providers

- OpenAI
- Google Gemini
- Groq
- OpenRouter

The active provider is selected using:

```env
LLM_PROVIDER=openai
```

---

# Architecture

The project follows a Domain-Driven architecture.

```
domains
├── companies
├── finance
└── research
```

Key design principles:

- Domain Separation
- Dependency Injection
- Provider Pattern
- Factory Pattern
- Clean Architecture
- Testable Services

---

# Development Workflow

Before committing code:

```bash
uv run ruff check . --fix

uv run ruff format .

uv run pytest
```

---

# Tech Stack

- Python 3.12
- LangChain
- LangGraph
- DeepAgents
- OpenAI
- Gemini
- Groq
- OpenRouter
- Tavily
- Yahoo Finance
- Streamlit
- uv
- Ruff
- Pytest

---

# License

Proprietary © AgentOps Africa