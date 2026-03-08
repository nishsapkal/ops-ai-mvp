🧠 AI Incident Investigation Agent (RAG + Agentic AI)
🚀 Enterprise-Grade AI Investigation Engine for Integration & Platform Incidents

I built this to solve a real problem I see in enterprise integration platforms — ops teams spending hours manually correlating Kafka metrics, logs, and incident history. This agent automates that triage usinga multi-agent RAG architecture.

This project demonstrates a minimal production-style AI Incident Investigation Agent combining:


Retrieval Augmented Generation (RAG)

Multi-Tool Agent Orchestration

AI Planning & Tool Selection

Parallel Evidence Collection

Self-Evaluation & Confidence Checking

Incident Memory Learning Loop

Designed with Enterprise Integration Platforms in mind.

🎯 Problem Statement

Modern integration platforms generate massive telemetry:

Logs

Kafka Metrics

Error Traces

Incident Knowledge Base

Ops teams spend hours correlating signals.

This project demonstrates how AI Agents can automate incident triage and root cause hypothesis generation.

🏗 Architecture Overview
User Incident Query
↓
Planner Agent (LLM decides investigation plan)
↓
Dynamic Tool Selection
↓
Parallel Tool Execution
   ├ Knowledge Base (RAG)
   ├ Log Analyzer
   ├ Kafka Metrics Checker
↓
Evidence Aggregation
↓
Reasoning Agent
↓
Self Evaluation Agent
↓
Final Root Cause + Fix Suggestion

🧩 Core Capabilities
🧠 Planner Agent

Uses LLM to decide:

Which tools to call

Investigation strategy

🔎 RAG Knowledge Retrieval

Vector search over incident knowledge base.

Tech:

Chroma Vector DB

OpenAI Embeddings

Semantic Retrieval

⚙ Dynamic Tool Orchestration

No hardcoded if/else routing.

Tools selected based on incident context.

⚡ Parallel Evidence Collection

Tools executed concurrently for low latency.

🧪 Self Evaluation Layer

AI verifies:

Evidence support

Confidence justification

Hallucination risk

🧠 Incident Memory

Stores past investigations to improve reasoning context.

📁 Project Structure
rag-lab/
│
├ incident_agent_v2.py       # Main Agent Runtime
├ planner.py                 # Investigation Planning Agent
├ tool_registry.py           # Tool Discovery Layer
├ executor.py                # Parallel Tool Execution
├ self_evaluator.py          # AI Self Quality Check
├ memory_store.py            # Incident Memory
├ incident_tools.py          # Tool Implementations
│
├ metadata_extractor.py      # AI Metadata Classification
├ rag_ingestion.py           # RAG Knowledge Pipeline
│
├ data/                      # Sample Incident Dataset
├ chroma_db/                 # Vector Database Storage

🛠 Technology Stack
Layer	Technology
LLM	OpenAI GPT Models
Embeddings	OpenAI Embeddings
Vector DB	Chroma
Framework	LangChain
Execution	Python
Concurrency	ThreadPoolExecutor
🚀 How To Run
1️⃣ Setup Environment
python -m venv venv
source venv/bin/activate

2️⃣ Install Dependencies
pip install langchain langchain-community langchain-openai chromadb python-dotenv

3️⃣ Add OpenAI Key

Create .env

OPENAI_API_KEY=your_key_here

4️⃣ Build Knowledge Index
python rag_ingestion.py

5️⃣ Run Agent
python incident_agent_v2.py

🧪 Example Queries
Payment failures during peak load
Kafka lag causing order delay
Database timeout impacting API calls

*** DEMO Execution START ***

/opsai/incident_agent_main.py:110: LangChainDeprecationWarning: The class `Chroma` was deprecated in LangChain 0.2.9 and will be removed in 1.0. An updated version of the class exists in the langchain-chroma package and should be used instead. To use it run `pip install -U langchain-chroma` and import as `from langchain_chroma import Chroma`.
  vector_db = Chroma(
✅ Agent Ready!

Describe Incident (type exit to quit): describe payment issues

🧠 Step 1 — Planning Investigation...
🛠 Tools Selected: ['knowledge_base', 'logs']

⚙ Step 2 — Executing Tools...
📄 Evidence Collected: {'logs': 'Observed timeout errors in payment service logs', 'knowledge_base': ''}

🧠 Step 3 — Loading Past Incident Memory...

🤖 Step 4 — Final Reasoning...

🤖 Step 5 — Self Evaluation..

🧪 Self Evaluation: {'is_reliable': True, 'confidence_adjustment': 'same', 'reason': 'The evidence provided directly supports the answer given. The observed timeout errors in the payment service logs align with the suggested root cause of a bottleneck or failure in the payment service. The suggested fix also logically follows from the identified root cause.'}

🚨 INCIDENT ANALYSIS RESULT
1. Most Likely Root Cause:
   The most likely root cause of the payment issues is a bottleneck or failure in the payment service leading to timeout errors.

2. Confidence:
   Medium

3. Suggested Fix:
   Investigate the payment service to identify and resolve the bottleneck or failure causing the timeout errors. This may involve optimizing the service, increasing resources, or fixing any bugs in the code. Additionally, monitoring tools can be implemented to track performance and detect issues early on.

====================================================================== 
**** DEMO END ***

🧠 Real Enterprise Use Cases
Integration Platform AI Copilot

Auto root cause analysis for integration failures.

AI Ops Incident Assistant

Reduce MTTR by automated investigation.

Knowledge Intelligence Layer

Unified semantic search across incident history.

🔮 Future Enhancements

Async Tool Execution

Real Log Integration (ELK / Datadog)

Kafka Metrics API Integration

Human Feedback Learning Loop

Agent Planning Memory

Evaluation Metrics Dashboard

Multi-Agent Collaboration


