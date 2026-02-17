from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)


def self_evaluate(query, evidence, draft_answer):

    prompt = f"""
    You are an AI quality evaluator.

    Check:
    - Does evidence support answer?
    - Is answer guessing?
    - Is confidence justified?

    Query:
    {query}

    Evidence:
    {evidence}

    Answer:
    {draft_answer}

    Return JSON:
    {{
      "is_reliable": true/false,
      "confidence_adjustment": "increase/decrease/same",
      "reason": "..."
    }}
    """

    result = llm.invoke(prompt)

    import json
    try:
        return json.loads(result.content)
    except:
        return {
            "is_reliable": True,
            "confidence_adjustment": "same",
            "reason": "Evaluator failed"
        }
