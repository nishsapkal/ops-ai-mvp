from incident_tools import (
    search_incident_kb,
    analyze_logs,
    check_kafka_lag
)


def get_tool(tool_name):

    registry = {
        "knowledge_base": search_incident_kb,
        "logs": analyze_logs,
        "kafka": check_kafka_lag
    }

    return registry.get(tool_name)

