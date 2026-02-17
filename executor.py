import concurrent.futures


def execute_tools_parallel(tool_map, query, retriever):

    results = {}

    def run_tool(tool_name, tool_fn):

        try:
            if tool_name == "knowledge_base":
                return tool_name, tool_fn(query, retriever)
            else:
                return tool_name, tool_fn(query)

        except Exception as e:
            return tool_name, f"ERROR: {str(e)}"

    with concurrent.futures.ThreadPoolExecutor() as executor:

        futures = []

        for tool_name, tool_fn in tool_map.items():
            futures.append(executor.submit(run_tool, tool_name, tool_fn))

        for future in concurrent.futures.as_completed(futures):
            tool_name, result = future.result()
            results[tool_name] = result

    return results
