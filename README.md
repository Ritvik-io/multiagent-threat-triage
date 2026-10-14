# 🛡️ Local Multi-Agent Cybersecurity Threat Triage System

An end-to-end, privacy-focused AI application for cybersecurity threat research, document analysis, and executive reporting. Built with **Streamlit, LangGraph, LangChain, Ollama, HuggingFace, FAISS, and DuckDuckGo Search**, the system combines locally processed PDF documents with live web research to generate concise, AI-powered cybersecurity threat summaries.

## 📌 Key Features

- 🔒 **Local LLM Inference:** Uses Ollama with `llama3.2` to generate reports locally without paid cloud LLM APIs.
- 🖥️ **Interactive Streamlit Dashboard:** Provides a web interface for entering cybersecurity queries, uploading PDF documents, and viewing generated reports.
- 📄 **PDF-Based Threat Intelligence:** Extracts relevant information from uploaded security reports and documents.
- 🧠 **Retrieval-Augmented Generation (RAG):** Uses HuggingFace embeddings and FAISS to retrieve relevant document passages based on the user's query.
- 🌐 **Live Web Research:** Integrates DuckDuckGo Search (`ddgs`) to retrieve additional cybersecurity information from the web.
- 🤖 **Multi-Agent Orchestration:** Uses LangGraph to coordinate specialized agents through a structured workflow.
- 🔍 **Technical Research:** Combines findings from local documents and web searches to help identify relevant vulnerabilities, CVEs, and threat information.
- 📊 **Executive-Level Reporting:** Uses a local LLM to synthesize research findings into concise, readable summaries.

## 🏗️ System Architecture

```text
             ┌─────────────────────────────┐
             │   Streamlit Web Dashboard   │
             │                             │
             │  • Threat Query Input       │
             │  • PDF Document Upload      │
             └──────────────┬──────────────┘
                            │
                            ▼
             ┌─────────────────────────────┐
             │     Document Processing     │
             │                             │
             │  • PDF Text Extraction      │
             │  • Text Chunking            │
             │  • HuggingFace Embeddings   │
             │  • FAISS Vector Index       │
             └──────────────┬──────────────┘
                            │
                            ▼
             ┌─────────────────────────────┐
             │      Researcher Agent       │
             │                             │
             │  • Local PDF Retrieval      │
             │  • DuckDuckGo Web Search    │
             │  • Research Consolidation   │
             └──────────────┬──────────────┘
                            │
                            ▼
             ┌─────────────────────────────┐
             │        Writer Agent         │
             │                             │
             │  • Ollama: llama3.2         │
             │  • Research Synthesis       │
             │  • Executive Summarization  │
             └──────────────┬──────────────┘
                            │
                            ▼
             ┌─────────────────────────────┐
             │     Final Threat Report     │
             │                             │
             │  • Key Findings              │
             │  • Threat Summary            │
             │  • Relevant Evidence         │
             └─────────────────────────────┘
```

## 🔄 How It Works

1. **User Input:** The user enters a cybersecurity threat query through the Streamlit dashboard and optionally uploads relevant PDF reports.
2. **Document Processing:** The application extracts PDF text, divides it into smaller chunks, generates embeddings using `all-MiniLM-L6-v2`, and indexes the embeddings using FAISS.
3. **Researcher Agent:** Retrieves relevant passages from the local document index and gathers supplementary information through DuckDuckGo Search.
4. **Writer Agent:** Uses the locally running `llama3.2` model through Ollama to synthesize the available research into an executive-level report.
5. **Report Generation:** The resulting summary is displayed through the Streamlit interface.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Core programming language |
| Streamlit | Interactive web dashboard |
| LangGraph | Multi-agent workflow orchestration |
| LangChain | LLM and retrieval integration |
| Ollama | Local model inference |
| Llama 3.2 | Threat report generation |
| HuggingFace `all-MiniLM-L6-v2` | Text embeddings |
| FAISS | Vector indexing and similarity search |
| PyPDF | PDF text extraction, if used by the implementation |
| DuckDuckGo Search (`ddgs`) | Live web information retrieval |

## 🚀 Getting Started

### Prerequisites

Ensure the following are installed:

- Python 3.12
- Git
- [Ollama](https://ollama.com/)

### 1. Download the Local Language Model

Open PowerShell and run:

```powershell
ollama pull llama3.2
```

Ensure Ollama is running before launching the application.

### 2. Clone the Repository

```powershell
git clone https://github.com/Ritvik-io/multiagent-threat-triage.git
cd multiagent-threat-triage
```

### 3. Create and Activate a Virtual Environment

```powershell
python -3.12 -m venv venv
.\venv\Scripts\Activate.ps1
```

If the `python -3.12` command is unavailable, ensure Python 3.12 is installed and accessible through the Python launcher.

### 4. Install Dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Launch the Application

```powershell
streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to access the dashboard.

## 💡 Example Use Cases

The system can assist with preliminary research into:

- Common Vulnerabilities and Exposures (CVE)
- Ransomware and malware campaigns
- Phishing attacks and social engineering
- Vulnerability information contained in uploaded security reports
- Emerging cybersecurity threats and attack vectors
- Technical security documents requiring concise executive summaries

## 🔐 Privacy and Security

- **Local inference:** The language model processes prompts locally through Ollama.
- **Local document retrieval:** PDF embeddings and FAISS indexing can run locally.
- **No paid cloud LLM required:** The core workflow uses a locally hosted language model.
- **External web retrieval:** DuckDuckGo searches require an internet connection and send search queries to an external service.
- **Sensitive documents:** Uploaded PDFs and extracted text should be handled carefully and should not be assumed to be protected merely because the LLM runs locally.

**Important:** Local model inference does not make the entire application offline. Web search requires internet access, and actual privacy depends on how the application handles uploaded files, logs, caches, and temporary data.

## 🔮 Future Improvements

Potential enhancements include:

- CVSS-based vulnerability prioritization.
- Integration with the official National Vulnerability Database (NVD) API.
- Source citations and evidence-linked findings.
- MITRE ATT&CK technique mapping.
- Structured JSON threat reports.
- PDF and Markdown report exports.
- Additional agents for vulnerability analysis and remediation recommendations.
- Automated evaluation of report accuracy and evidence quality.

## ⚠️ Disclaimer

This project is intended for educational purposes and defensive cybersecurity research. AI-generated findings may be incomplete or inaccurate. Verify vulnerabilities, severity assessments, and recommendations against authoritative security advisories before making security decisions.

## 👨‍💻 Author

**Ritvik Sharma**

GitHub: [Ritvik-io](https://github.com/Ritvik-io)

---

*Exploring the intersection of local AI, retrieval-augmented generation, multi-agent systems, and cybersecurity threat intelligence.*
