import os
import tempfile
import streamlit as st
from typing import TypedDict
from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import StateGraph, END

# --- Streamlit UI Page Config ---
st.set_page_config(page_title="Threat Triage Multi-Agent AI", page_icon="", layout="wide")
st.title(" Local Multi-Agent Threat Triage System")
st.caption("Powered by LangGraph, Ollama (llama3.2), DuckDuckGo, & Local PDF RAG")

# --- Step 1: Dynamic File Uploader & Topic Input ---
st.sidebar.header(" Document & Query Setup")
uploaded_file = st.sidebar.file_uploader("Upload a Threat Report PDF (Optional)", type=["pdf"])
topic_input = st.text_input("Enter Cybersecurity Topic / Threat Query:", "Multi-agent AI systems in cybersecurity threat triage")

# --- Helper: Index Uploaded PDF ---
def process_uploaded_pdf(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(file.getvalue())
        tmp_path = tmp_file.name

    loader = PyPDFLoader(tmp_path)
    docs = loader.load()
    os.remove(tmp_path)  # Cleanup temp file

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = text_splitter.split_documents(docs)

    # Use a lightweight local embedding model:
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(splits, embeddings)
    return vectorstore.as_retriever(search_kwargs={"k": 3})

# --- LangGraph Setup ---
llm = ChatOllama(model="llama3.2", temperature=0)
search_tool = DuckDuckGoSearchRun()

class AgentState(TypedDict):
    topic: str
    pdf_context: str
    web_context: str
    research_notes: str
    final_report: str

def create_workflow(pdf_retriever):
    def researcher_agent(state: AgentState) -> dict:
        topic = state["topic"]
        pdf_data = ""

        if pdf_retriever:
            pdf_docs = pdf_retriever.invoke(topic)
            pdf_data = "\n".join([doc.page_content for doc in pdf_docs])

        web_data = search_tool.run(topic)

        prompt = f"""
        You are an expert Security Threat Analyst.
        Synthesize technical facts, CVEs, tools, or techniques from the provided local documents and web data:

        LOCAL PDF CONTEXT:
        {pdf_data if pdf_data else "No PDF context uploaded."}

        LIVE WEB DATA:
        {web_data}
        """

        response = llm.invoke([
            SystemMessage(content="Extract concise, technical bullet points."),
            HumanMessage(content=prompt)
        ])

        return {
            "pdf_context": pdf_data,
            "web_context": web_data,
            "research_notes": response.content
        }

    def writer_agent(state: AgentState) -> dict:
        prompt = f"""
        You are a Technical Report Writer.
        Using ONLY the research notes provided below, write a clean 3-bullet-point executive summary report on '{state['topic']}':

        RESEARCH NOTES:
        {state['research_notes']}
        """

        response = llm.invoke([
            SystemMessage(content="Write clear, professional executive summaries."),
            HumanMessage(content=prompt)
        ])

        return {"final_report": response.content}

    workflow = StateGraph(AgentState)
    workflow.add_node("Researcher", researcher_agent)
    workflow.add_node("Writer", writer_agent)

    workflow.set_entry_point("Researcher")
    workflow.add_edge("Researcher", "Writer")
    workflow.add_edge("Writer", END)

    return workflow.compile()

# --- Execution ---
if st.button(" Run Threat Triage Pipeline", type="primary"):
    pdf_retriever = None

    if uploaded_file is not None:
        with st.spinner(" Processing uploaded PDF..."):
            pdf_retriever = process_uploaded_pdf(uploaded_file)
            st.sidebar.success("PDF Indexed Successfully!")

    app = create_workflow(pdf_retriever)

    initial_input = {
        "topic": topic_input,
        "pdf_context": "",
        "web_context": "",
        "research_notes": "",
        "final_report": ""
    }

    with st.spinner(" Agents are researching and generating the summary..."):
        output = app.invoke(initial_input)

    st.subheader("================ FINAL REPORT ================")
    st.markdown(output["final_report"])

    with st.expander(" View Raw Agent Findings"):
        st.write("**Research Notes:**", output["research_notes"])
        st.write("**Web Data:**", output["web_context"])
        if pdf_retriever:
            st.write("**PDF Context:**", output["pdf_context"])