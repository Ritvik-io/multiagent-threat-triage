# 🛡️ Local Multi-Agent Cybersecurity Threat Triage System

An end-to-end, privacy-focused AI system for cybersecurity threat research and executive reporting. Built using **LangGraph, LangChain, Ollama, and DuckDuckGo Search**, the system coordinates specialized AI agents to research cybersecurity threats and generate concise, structured reports using a locally running language model.

## 📌 Key Features

- **🔒 Local AI Inference:** Uses Ollama with `llama3.2` to generate reports locally without relying on paid cloud LLM APIs.
- **🌐 Live Threat Research:** Integrates DuckDuckGo Search through `ddgs` to retrieve relevant cybersecurity information from the web.
- **🤖 Multi-Agent Architecture:** Uses LangGraph to orchestrate specialized agents through a structured workflow.
- **🔍 Technical Fact Extraction:** Researches cybersecurity topics and organizes relevant technical findings into research notes.
- **📊 Executive Reporting:** Converts technical research into concise, three-bullet executive summaries.
- **🧩 Modular Workflow:** Separates research and report generation into distinct agent nodes for easier maintenance and future expansion.

## 🏗️ Architecture

```text
             ┌──────────────────────────┐
             │       User Topic         │
             └────────────┬─────────────┘
                          │
                          ▼
             ┌──────────────────────────┐
             │    Researcher Agent      │
             │                          │
             │  • DuckDuckGo Search     │
             │  • Information Retrieval │
             │  • Technical Fact Mining │
             └────────────┬─────────────┘
                          │
                          ▼
             ┌──────────────────────────┐
             │      Writer Agent        │
             │                          │
             │  • Ollama: llama3.2      │
             │  • Research Synthesis    │
             │  • Executive Summaries   │
             └────────────┬─────────────┘
                          │
                          ▼
             ┌──────────────────────────┐
             │   Final Threat Report    │
             │                          │
             │  • Three Key Takeaways   │
             │  • Concise Findings      │
             └──────────────────────────┘
```

### Agent Responsibilities

**1. Researcher Agent**
- Searches the web for information relevant to the user's cybersecurity topic.
- Collects and organizes technical findings from search results.
- Passes research notes to the next agent.

**2. Writer Agent**
- Uses the locally running `llama3.2` model through Ollama.
- Synthesizes the research notes into a readable executive summary.
- Produces a concise, three-bullet threat report.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Core programming language |
| LangGraph | Agent workflow orchestration |
| LangChain | LLM integration and application components |
| Ollama | Local language model inference |
| Llama 3.2 | Text generation and report synthesis |
| DuckDuckGo Search (`ddgs`) | Web-based information retrieval |
| Python-dotenv | Environment variable management |

## 🚀 Getting Started

### Prerequisites

Install the following before running the project:

- Python 3.12
- [Ollama](https://ollama.com/)
- Git

### 1. Download the Local Model

Open PowerShell and run:

```powershell
ollama pull llama3.2
```

Ensure Ollama is running before executing the application.

### 2. Clone the Repository

```powershell
git clone https://github.com/Ritvik-io/multiagent-threat-triage.git
cd multiagent-threat-triage
```

### 3. Create a Virtual Environment

```powershell
python -3.12 -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, consult the [Python virtual environment documentation](https://docs.python.org/3/library/venv.html).

### 4. Install Dependencies

```powershell
python -m pip install --upgrade pip
pip install langgraph langchain-ollama langchain-community ddgs python-dotenv
```

### 5. Run the Application

```powershell
python MultiAgent.py
```

Follow the application's prompts, if provided, to research a cybersecurity topic and generate a threat report.

## 💡 Example Use Cases

The system can be used to research topics such as:

- Common Vulnerabilities and Exposures (CVE)
- Ransomware and emerging malware campaigns
- Phishing techniques and social engineering
- Vulnerability trends and attack vectors
- Cybersecurity incidents and threat developments

*The quality and freshness of results depend on the available search results, the model, and the implementation.*

## 🔐 Privacy and Security

- The language model runs locally through Ollama.
- Research and report generation do not require a paid cloud LLM API.
- Web searches still send search queries to an external search provider.
- Retrieved web content should be treated as untrusted input.
- AI-generated findings should be verified against reliable sources before being used for security decisions.

**Note:** Local inference does not mean the entire workflow is offline. Live web research requires an internet connection.

## 🔮 Future Improvements

Potential enhancements include:

- Integration with the official NVD CVE API.
- CVSS severity scoring and vulnerability prioritization.
- Source URLs and evidence citations in generated reports.
- MITRE ATT&CK technique mapping.
- Structured JSON output for downstream security tools.
- Automated report export to Markdown or PDF.
- Additional specialized agents for vulnerability analysis and remediation recommendations.
- Evaluation tests for factual accuracy and source reliability.

## ⚠️ Disclaimer

This project is intended for educational cybersecurity research and defensive threat intelligence. AI-generated reports may contain inaccurate or incomplete information. Verify findings with trusted security advisories and authoritative sources before taking action.

## 👨‍💻 Author

**Ritvik Sharma**

GitHub: [Ritvik-io](https://github.com/Ritvik-io)

---

*Built to explore local AI, multi-agent orchestration, and cybersecurity threat intelligence.*
