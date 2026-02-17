incident_memory = []


def store_incident(query, findings):

    incident_memory.append({
        "query": query,
        "findings": findings
    })


def get_past_similar_incidents():

    return incident_memory[-3:]

