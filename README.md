# 🧠 SyntaxIQ — AI-Powered Codebase Intelligence

### Understand Any Repo. Any Language. Any Syntax.

<p align="center">
  <strong>An AI-powered workspace to explore, understand, and investigate codebases using natural language.</strong>
</p>

<p align="center">
  <a href="https://ai-codebase-agent-1-a2evlt6j7-shivraj-s-projects4.vercel.app">
    🚀 <strong>Try SyntaxIQ — Live Demo</strong>
  </a>
  &nbsp; • &nbsp;
  <a href="https://github.com/dharmeshsharma8085/ai-codebase-agent">
    💻 Source Code
  </a>
</p>

> [!WARNING]
> **🚧 SYNTAXIQ IS CURRENTLY UNDER DEVELOPMENT AND IS NOT READY FOR PRODUCTION USE.**
>
> A live deployment is available for preview and experimentation. We are actively improving the application's functionality, reliability, indexing pipeline, and user experience.
>
> **The deployed version may have limitations or errors. Do not rely on it for production workloads.**

---

## 🖥️ Project Preview

![SyntaxIQ UI Preview](asset/Screenshot.png)

*SyntaxIQ's dark-themed developer workspace.*

🌐 **Live Demo:** [Launch SyntaxIQ](https://ai-codebase-agent-1-a2evlt6j7-shivraj-s-projects4.vercel.app)

💻 **GitHub Repository:** [dharmeshsharma8085/ai-codebase-agent](https://github.com/dharmeshsharma8085/ai-codebase-agent)

---

## 📌 About SyntaxIQ

**SyntaxIQ** is an AI-powered codebase intelligence platform designed to help developers understand, explore, and investigate software repositories through natural language.

Working with an unfamiliar codebase can be challenging. Developers often need to navigate multiple files, trace function calls, understand dependencies, and investigate how different components interact.

SyntaxIQ aims to simplify this process by combining **Retrieval-Augmented Generation (RAG), Large Language Models (LLMs), and specialized AI agents** to answer questions using relevant repository code.

Instead of manually searching through an entire project, developers can ask questions such as:

- How does this project work?
- Explain the architecture of this repository.
- Where is a particular function implemented?
- How does data flow through the application?
- Which dependencies does this project use?
- Help me investigate a bug.
- Which files might be affected by a proposed change?
- Explain the responsibilities of important modules.

The goal is to make codebases easier to understand, navigate, debug, and maintain.

## 🎯 The Problem We're Solving

Understanding an unfamiliar repository can require hours of manual exploration.

Developers frequently need to:

- Search through multiple files to understand application logic.
- Trace dependencies and relationships between modules.
- Identify entry points and execution flow.
- Investigate bugs across different components.
- Understand unfamiliar functions, classes, and libraries.

SyntaxIQ aims to reduce this complexity by allowing developers to interact with repository code using natural language.

## ✨ Key Features

### Current Development Capabilities

- 🔗 **GitHub Repository Input** — Provide a public GitHub repository URL.
- 💬 **AI Codebase Chat** — Ask natural-language questions about a repository.
- 🔍 **Code Retrieval** — Retrieve relevant code chunks using embeddings and vector search.
- 🧩 **AST-Based Extraction** — Extract Python functions, classes, imports, and source ranges.
- 🗄️ **Vector Storage** — Store and retrieve code embeddings using ChromaDB.
- 🤖 **Agent-Based Workflow** — Route questions through specialized LangGraph agent paths.
- 🏗️ **Architecture Analysis** — Explain repository components and execution flow using available code context.
- 🐛 **Debugging Assistance** — Investigate potential root causes and suggest fixes.
- 🎨 **Dark-Themed Interface** — Interact with SyntaxIQ through a Streamlit UI.
- 📂 **Code References** — Surface likely file references from AI responses.

*These capabilities are under active development and may have limitations. They have not all been validated for production-level reliability.*

### 🔮 Planned Features

- 🌐 Multi-language code understanding.
- 🗂️ Interactive repository file explorer.
- 🏗️ Architecture and dependency visualization.
- 🔗 Function and module relationship analysis.
- 🛠️ Feature impact analysis and code improvement suggestions.
- 📝 Automated documentation generation.
- 🔐 Security analysis and testing assistance.
- 🐙 GitHub issues and pull request integration.
- 🧪 Improved automated testing and retrieval evaluation.
- ☁️ More reliable deployment and production infrastructure.

---

## 🏗️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | User interface |
| FastAPI | Backend API |
| LangGraph | Agent orchestration |
| LangChain | LLM integration and retrieval utilities |
| OpenAI API | Language model and embedding integration |
| OpenAI `text-embedding-3-small` | Code embeddings |
| ChromaDB | Vector database |
| GitPython | Repository cloning and Git operations |
| Python AST | Python code structure extraction |
| Git & GitHub | Version control and source hosting |
| uv | Python package and environment management |

---

## 🧠 System Architecture

SyntaxIQ follows a retrieval-based code understanding workflow.

```text
                         USER
                          |
                          v
                  STREAMLIT FRONTEND
                          |
                          v
                     FASTAPI API
                          |
                          v
                   CODEBASE SERVICE
                          |
                          v
                  LANGGRAPH WORKFLOW
                          |
                          v
                  SPECIALIZED AGENTS
                          |
                          v
                      RAG PIPELINE
                          |
                 +--------+--------+
                 |                 |
                 v                 v
           CODE RETRIEVAL      LLM REASONING
                 |                 |
                 v                 |
              CHROMADB             |
                 |                 |
                 +--------+--------+
                          |
                          v
                  REPOSITORY ANSWER
                 WITH CODE CONTEXT
```

### 🔄 RAG Pipeline

The repository indexing and question-answering pipeline is designed around these stages:

1. Accept a public GitHub repository URL.
2. Clone or update the repository locally.
3. Discover and load supported source files.
4. Parse code and extract structural information.
5. Create code-aware chunks with metadata.
6. Generate embeddings for the chunks.
7. Store embeddings in ChromaDB.
8. Retrieve relevant chunks for a user question.
9. Provide retrieved context to the LLM.
10. Return an answer based on the available code context.

The goal is to provide more repository-specific answers than a general-purpose chatbot working without source code.

---

## 🤖 AI Agent Architecture

SyntaxIQ includes four specialized agent paths in its current development architecture.

| Agent | Responsibility |
|---|---|
| Explorer Agent | Explains repository structure, files, functions, classes, and code flow |
| Debugger Agent | Investigates potential root causes and proposes fixes |
| Architecture Agent | Explains components, dependencies, and execution flow |
| Coding Agent | Suggests implementation changes and explains their impact |

LangGraph orchestrates the workflow and routes questions to the appropriate agent path.

**Note:** Autonomous code modification, automatic test execution, and pull request creation are not currently claimed as implemented features.

---

## 📁 Project Structure

The project follows a modular structure that separates the API, agents, workflow orchestration, RAG pipeline, and user interface.

```text
REPO ANALYSIS/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── api/
│       ├── __init__.py
│       └── routes.py
│
├── agents/
│   ├── explorer_agent.py
│   ├── debugger_agent.py
│   ├── architecture.py
│   ├── coding.py
│   └── utils.py
│
├── graph/
│   ├── state.py
│   ├── nodes.py
│   └── workflow.py
│
├── rag/
│   ├── loader.py
│   ├── cleaning.py
│   ├── extraction.py
│   ├── chunking.py
│   ├── embedding.py
│   ├── vectorstore.py
│   ├── retriever.py
│   ├── prompt.py
│   └── llm.py
│
├── services/
│   └── codebase_service.py
│
├── asset/
│   └── Screenshot.png
│
├── ui.py
├── test.py
├── test_graph.py
├── test_service.py
├── test_chunking.py
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
```

*This structure reflects the development setup documented for the project. The actual repository may evolve as development continues.*

---

## ⚙️ Getting Started

You can run the development version locally by following these instructions.

### Prerequisites

- Python 3.12 or a compatible Python version.
- Git.
- `uv` package manager.
- An OpenAI API key with the required API access and billing configured.

### 1. Clone the Repository

```bash
git clone https://github.com/dharmeshsharma8085/ai-codebase-agent.git

cd ai-codebase-agent
```

### 2. Install Dependencies

```bash
uv sync
```

If a required dependency is missing from `pyproject.toml`, add it using `uv add package-name`.

### 3. Configure Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Replace the placeholder with your own API key.

**Security reminder:** Never commit your actual `.env` file, API keys, or other credentials to GitHub. Keep `.env` in `.gitignore`.

### 4. Start the FastAPI Backend

Open a terminal in the project root:

```bash
uv run uvicorn app.main:app --reload
```

The local backend should be available at:

- **API:** `http://127.0.0.1:8000`
- **Interactive API documentation:** `http://127.0.0.1:8000/docs`

### 5. Start the Streamlit Frontend

Open a second terminal in the same project directory:

```bash
uv run streamlit run ui.py
```

Open the application in your browser:

`http://localhost:8501`

### 6. Ask a Repository Question

1. Enter a public GitHub repository URL in the UI.
2. Click **Load Repository**.
3. Ask a question or choose an available analysis action.
4. Wait for the backend to process the request and return an answer.

The first request may take longer if the repository needs to be cloned and indexed.

**Important:** Local setup requirements may differ from the hosted deployment configuration.

---

## 🔌 API Documentation

The current backend exposes a repository question-answering endpoint.

**Endpoint:** `POST /api/ask`

### Example Request

```json
{
  "repo_url": "https://github.com/owner/repository",
  "question": "Explain the architecture of this project."
}
```

### Example Response

```json
{
  "response": "The generated repository analysis..."
}
```

The response depends on the selected repository, retrieved code, model output, and current implementation.

For local API documentation, visit:

`http://127.0.0.1:8000/docs`

---

## 🗺️ Development Roadmap

### Core System

- [x] Initial FastAPI backend.
- [x] LangGraph workflow and agent paths.
- [x] Initial repository loading pipeline.
- [x] Python AST extraction and code-aware chunking.
- [x] ChromaDB integration and retrieval.
- [x] Initial Streamlit interface.
- [x] Frontend connection to the existing API.

### Improvements in Progress

- [ ] Improve indexing reliability and stale-index handling.
- [ ] Improve retrieval quality and verified source references.
- [ ] Add robust multi-language parsing.
- [ ] Build a verified repository browser.
- [ ] Add architecture and dependency visualization.
- [ ] Expand automated tests and error handling.
- [ ] Improve deployment configuration and production safeguards.

### Future Direction

- [ ] GitHub issues and pull request integration.
- [ ] Advanced code analysis and impact assessment.
- [ ] Better repository-level testing assistance.
- [ ] Production-ready infrastructure and monitoring.

*Roadmap items may change as the project evolves.*

---

## 🚧 Development Status

**SYNTAXIQ IS CURRENTLY UNDER ACTIVE DEVELOPMENT AND IS NOT READY FOR PRODUCTION USE.**

A live deployment is available for preview and experimentation.

### 🚀 Try the Live Demo

**[Open SyntaxIQ](https://ai-codebase-agent-1-a2evlt6j7-shivraj-s-projects4.vercel.app)**

We are continuing to improve:

- Repository indexing and retrieval reliability.
- AI-generated answers and code references.
- Error handling and application stability.
- Multi-language code understanding.
- User experience and interface design.
- Deployment configuration and production safeguards.

The deployed version may not support every feature reliably. Please use it for preview and experimentation rather than production workloads.

**We will continue improving SyntaxIQ and updating the live version as development progresses.**

Thank you for checking out the project and following its development! ❤️

---

## 🔒 Security and Limitations

- Do not submit API keys, passwords, or other secrets inside repository code or questions.
- Never commit `.env` files or credentials.
- The current indexing implementation primarily supports Python source files.
- Repository answers may be incomplete or incorrect.
- File references extracted from responses should be verified against the actual repository.
- Repository metadata and file-tree features may not yet be available.
- Production deployment, comprehensive security testing, and multi-language support are still in progress.

**Please do not use the current deployment for sensitive source code or production-critical workloads.**

---

## 👨‍💻 Developer

**Dharmesh Sharma**

AI Engineering student building practical applications involving LLMs, RAG, agentic workflows, and software engineering.

- **GitHub:** [@dharmeshsharma8085](https://github.com/dharmeshsharma8085)
- **Project Repository:** [SyntaxIQ — AI Codebase Intelligence](https://github.com/dharmeshsharma8085/ai-codebase-agent)
- **Live Demo:** [Try SyntaxIQ](https://ai-codebase-agent-1-a2evlt6j7-shivraj-s-projects4.vercel.app)

---

## ⭐ Support the Project

If you find the idea interesting, consider starring the repository on GitHub.

Feedback, suggestions, and contributions are welcome as SyntaxIQ continues to evolve.

---

<p align="center">
  <strong>Built with curiosity, code, and AI. 🧠</strong>
  <br><br>
  <em>SyntaxIQ — Understand Any Repo. Any Language. Any Syntax.</em>
</p>