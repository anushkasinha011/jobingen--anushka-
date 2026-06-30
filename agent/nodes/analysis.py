def analysis_node(state):

    state["analysis"] = {
        "total_trends": len(state.get("trends", [])),
        "total_news": len(state.get("news", [])),
        "total_reddit": len(state.get("reddit", []))
    }

    return state