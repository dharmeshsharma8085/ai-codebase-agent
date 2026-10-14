https://ai-codebase-agent-1-a2evlt6j7-shivraj-s-projects4.vercel.app
# 🧠 SyntaxIQ — AI-Powered Codebase Intelligence

**Understand Any Repo. Any Language. Any Syntax.**

> [!WARNING]
> **🚧 SYNTAXIQ IS CURRENTLY UNDER DEVELOPMENT AND IS NOT READY FOR PRODUCTION USE.**
>
> We are actively working on improving the application, testing its functionality, and preparing for deployment. The project is not production-ready yet.
>
> **A working live demo link will be shared as soon as possible. Stay tuned! 🚀**

---

## 🖥️ Project Preview

![SyntaxIQ UI Preview](asset/Screenshot.png)

*SyntaxIQ's dark-themed developer workspace — currently under active development.*

---

## 📌 About the Project

**SyntaxIQ** is an AI-powered codebase intelligence platform designed to help developers understand, explore, and investigate software repositories using natural language.

Understanding an unfamiliar codebase can be time-consuming. Developers often need to navigate multiple files, trace function calls, understand dependencies, and investigate how different components interact.

SyntaxIQ aims to simplify this process by combining **Retrieval-Augmented Generation (RAG), Large Language Models (LLMs), and specialized AI agents** to answer questions using relevant repository code.

Instead of manually searching through an entire project, developers will be able to ask questions such as:

- How does this project work?
- Explain the architecture of this repository.
- Where is a particular function implemented?
- How does data flow through the application?
- Which dependencies does this project use?
- Help me investigate a bug.
- Which files might be affected by a proposed change?

The goal is to make codebases easier to understand, navigate, and maintain.

## ✨ Key Features

### Currently Implemented in the Development Prototype

- 🔗 **GitHub Repository Input** — Provide a public GitHub repository URL.
- 💬 **AI Codebase Chat** — Ask natural-language questions about a repository.
- 🔍 **Code Retrieval** — Retrieve relevant code chunks using embeddings and vector search.
- 🧩 **AST-Based Extraction** — Extract Python functions, classes, imports, and source ranges.
- 🗄️ **Vector Storage** — Store and retrieve code embeddings using ChromaDB.
- 🤖 **Agent-Based Workflow** — Route questions through specialized LangGraph agent paths.
- 🎨 **Dark-Themed UI** — Interact with SyntaxIQ through a Streamlit interface.
- 📂 **Code References** — Surface likely file references from AI responses.

*These capabilities are under active development and may have limitations. Their presence does not imply production-level reliability.*

### Planned Features

- 🌐 Multi-language code understanding.
- 🗂️ Interactive repository file explorer.
- 🏗️ Architecture and dependency visualization.
- 🐛 Deeper bug investigation and debugging assistance.
- 🔗 Function and module relationship analysis.
- 🛠️ Feature impact analysis and code improvement suggestions.
- 📝 Automated documentation generation.
- 🔐 Security analysis and testing assistance.
- 🐙 GitHub issues and pull request integration.
- ☁️ Public deployment and a live demo.

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
| GitPython | GitHub repository cloning and updates |
| Python AST | Python code structure extraction |
| Git & GitHub | Version control and source hosting |
| uv | Python package and environment management |

## 🧠 System Architecture

SyntaxIQ follows a retrieval-based code understanding workflow.

```text
                  User
                   |
                   v
          Streamlit Frontend
                   |
                   v
             FastAPI API
                   |
                   v
          Codebase Service
                   |
                   v
         LangGraph Workflow
                   |
                   v
          Specialized Agents
                   |
                   v
             RAG Pipeline
                   |
        +----------+----------+
        |                     |
        v                     v
  Code Retrieval         LLM Reasoning
        |                     |
        v                     |
     ChromaDB                 |
        |                     |
        +----------+----------+
                   |
                   v
          Repository Answer
          with File References
```

### RAG Pipeline

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
10. Return an answer grounded in the available code context.

## 🤖 AI Agent Architecture

SyntaxIQ includes four specialized agent paths in its current development architecture.

| Agent | Responsibility |
|---|---|
| Explorer Agent | Explains repository structure, files, functions, classes, and code flow |
| Debugger Agent | Investigates potential root causes and proposes fixes |
| Architecture Agent | Explains components, dependencies, and execution flow |
| Coding Agent | Suggests implementation changes and explains their impact |

LangGraph orchestrates the workflow and routes questions to the appropriate agent path.

**Note:** Advanced autonomous coding, automatic file modification, automated testing, and pull request creation are not yet claimed as implemented capabilities.

## 📁 Project Structure

The project is organized into modular components.

```text
REPO ANALYSIS/
│
├── app/
│   ├── main.py
│   └── api/
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

*This is the intended documented structure based on the current development setup. Your local files may differ as development continues.*

## ⚙️ Getting Started

### Prerequisites

Install the following before running the project:

- Python 3.12 or a compatible Python version.
- Git.
- `uv` package manager.
- An OpenAI API key with the required API access and billing configured.

### 1. Clone the repository

```bash
git clone https://github.com/dharmeshsharma8085/ai-codebase-agent.git
cd ai-codebase-agent
```

### 2. Install dependencies

```bash
uv sync
```

If a required dependency is missing from `pyproject.toml`, add it through `uv add package-name` rather than installing it into an unrelated Python environment.

### 3. Configure environment variables

Create a `.env` file in the project root and configure the variables expected by the current application.

For example:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Never commit your actual `.env` file or API keys to GitHub. Keep `.env` in `.gitignore`.

### 4. Start the FastAPI backend

Open a terminal in the project root:

```bash
uv run uvicorn app.main:app --reload
```

The backend should be available at:

- API: `http://127.0.0.1:8000`
- Interactive API documentation: `http://127.0.0.1:8000/docs`

### 5. Start the Streamlit frontend

Open a second terminal in the same project directory:

```bash
uv run streamlit run ui.py
```

Open the local application at:

`http://localhost:8501`

### 6. Ask a repository question

1. Enter a public GitHub repository URL in the UI.
2. Click **Load Repository**.
3. Ask a question or choose an analysis action.
4. Wait for the backend to process the request and return an answer.

The first request may take longer if the repository needs to be cloned and indexed.

## 🔌 API Endpoint

The current backend exposes a repository question-answering endpoint.

**Endpoint:** `POST /api/ask`

Example request:

```json
{
  "repo_url": "https://github.com/owner/repository",
  "question": "Explain the architecture of this project."
}
```

The endpoint returns a JSON response containing the answer:

```json
{
  "response": "The generated repository analysis..."
}
```

The actual answer depends on the repository, retrieved code, model response, and current implementation.

## 🗺️ Development Roadmap

- [x] Initial FastAPI backend.
- [x] LangGraph workflow and agent paths.
- [x] Initial repository loading pipeline.
- [x] Python AST extraction and code-aware chunking.
- [x] ChromaDB integration and retrieval.
- [x] Initial Streamlit interface.
- [x] Frontend connection to the existing API.
- [ ] Improve indexing reliability and stale-index handling.
- [ ] Improve retrieval quality and verified source references.
- [ ] Add robust multi-language parsing.
- [ ] Build a verified repository browser and architecture visualization.
- [ ] Expand automated tests and error handling.
- [ ] Add deployment configuration and production safeguards.
- [ ] Deploy a working public demo.

## 🚧 Development Status

**SyntaxIQ is an active work-in-progress and is NOT READY FOR PRODUCTION.**

The current implementation is a development prototype. Features, indexing behavior, answer quality, and error handling still require further testing and improvement.

We are actively developing the project and working toward a stable, publicly accessible version.

**A working deployed link will be provided as soon as possible. Thank you for your patience and support!**

Until then, you can explore the source code and run the application locally by following the setup instructions above.

## 🔒 Security and Limitations

- Do not submit API keys, passwords, or other secrets inside repository code or questions.
- Never commit `.env` files or credentials.
- The current indexing implementation primarily supports Python source files.
- Repository answers depend on retrieved context and may be incomplete or incorrect.
- File references extracted from responses should be verified against the actual repository.
- Production deployment, comprehensive security testing, and multi-language support are still in progress.

## 👨‍💻 Developer

**Dharmesh Sharma**

AI Engineering student building practical applications involving LLMs, RAG, agentic workflows, and software engineering.

- GitHub: [@dharmeshsharma8085](https://github.com/dharmeshsharma8085)
- Project repository: [SyntaxIQ — AI Codebase Intelligence](https://github.com/dharmeshsharma8085/ai-codebase-agent)

## ⭐ Support the Project

If you find the idea interesting, consider starring the repository on GitHub. Feedback, suggestions, and contributions are welcome as SyntaxIQ continues to evolve.

---

**Built with curiosity, code, and AI. 🧠**

*SyntaxIQ — Understand Any Repo. Any Language. Any Syntax.*
