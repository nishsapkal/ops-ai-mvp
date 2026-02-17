from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)


def plan_investigation(query):

    prompt = f"""
    You are an Incident Investigation Planner.

    Decide which tools to use.

    Available Tools:
    - knowledge_base
    - logs
    - kafka

    Return JSON:
    {{
      "tools": ["tool1", "tool2"]
    }}

    Query:
    {query}
    """

    response = llm.invoke(prompt)

    import json
    try:
        return json.loads(response.content)
    except:
        return {"tools": ["knowledge_base"]}

