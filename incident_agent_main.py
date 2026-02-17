import json
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

from planner import plan_investigation
from tool_registry import get_tool
from memory_store import store_incident, get_past_similar_incidents
from executor import execute_tools_parallel
from self_evaluator import self_evaluate



# =============================
# LLM INIT
# =============================

llm = ChatOpenAI(temperature=0)


# =============================
# CORE AGENT LOGIC
# =============================

def incident_agent(query, retriever):

    print("\n🧠 Step 1 — Planning Investigation...")

    try:
        plan = plan_investigation(query)
        tool_names = plan.get("tools", [])
    except Exception as e:
        print("⚠ Planner failed, defaulting to KB only:", e)
        tool_names = ["knowledge_base"]

    print("🛠 Tools Selected:", tool_names)

    # Build tool execution map
    tool_map = {}
    for tool_name in tool_names:
        tool_fn = get_tool(tool_name)
        if tool_fn:
            tool_map[tool_name] = tool_fn

    print("\n⚙ Step 2 — Executing Tools...")

    try:
       # evidence = execute_tools(tool_map, query, retriever)
        evidence = execute_tools_parallel(tool_map, query, retriever)
        
    except Exception as e:
        print("⚠ Tool execution failed:", e)
        evidence = {}

    print("📄 Evidence Collected:", evidence)

    print("\n🧠 Step 3 — Loading Past Incident Memory...")
    past_incidents = get_past_similar_incidents()

    print("\n🤖 Step 4 — Final Reasoning...")

    final_prompt = f"""
    You are an Enterprise Incident Investigation AI.

    INCIDENT:
    {query}

    EVIDENCE FROM TOOLS:
    {json.dumps(evidence, indent=2)}

    PAST INCIDENTS:
    {json.dumps(past_incidents, indent=2)}

    Provide:
    1. Most Likely Root Cause
    2. Confidence (Low / Medium / High)
    3. Suggested Fix
    """

    result = llm.invoke(final_prompt)

    print("\n🤖 Step 5 — Self Evaluation..")

    evaluation = self_evaluate(query, evidence, result.content)

    print("\n🧪 Self Evaluation:", evaluation)


    # Store memory
    store_incident(query, evidence)

    return result.content


# =============================
# RUNNER
# =============================

def run_agent():

    load_dotenv()

    print("\n🚀 Starting Incident Investigation Agent...\n")

    # Load Vector DB
    embedding = OpenAIEmbeddings()

    try:
        vector_db = Chroma(
            persist_directory="./chroma_db",
            embedding_function=embedding
        )
    except Exception as e:
        print("❌ Failed to load Chroma DB:", e)
        return

    retriever = vector_db.as_retriever(search_kwargs={"k": 3})

    print("✅ Agent Ready!\n")

    while True:

        query = input("Describe Incident (type exit to quit): ")

        if query.lower() == "exit":
            print("👋 Exiting Agent...")
            break

        try:
            result = incident_agent(query, retriever)

            print("\n🚨 INCIDENT ANALYSIS RESULT")
            print(result)
            print("\n" + "=" * 70 + "\n")

        except Exception as e:
            print("❌ Agent Execution Failed:", e)


# =============================
# ENTRY POINT
# =============================

if __name__ == "__main__":
    run_agent()

