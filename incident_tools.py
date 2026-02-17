def search_incident_kb(query, retriever):
    docs = retriever.invoke(query)

    results = []
    for d in docs:
        results.append(d.page_content)

    return "\n".join(results)


def analyze_logs(service_name):
    # Simulated for now (later connect ELK / Datadog etc)

    if "payment" in service_name.lower():
        return "Observed timeout errors in payment service logs"

    if "order" in service_name.lower():
        return "Observed DB connection pool saturation in logs"

    return "No major errors found"


def check_kafka_lag(topic):
    # Simulated for now (later connect Kafka metrics)

    if "order" in topic.lower():
        return "High consumer lag detected"

    return "Lag normal"

