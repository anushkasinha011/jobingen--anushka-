def platform_strategist_node(state):

    strategies = []

    for item in state.get("scored_trends", []):

        strategies.append({
            "topic": item["topic"],
            "platform": "LinkedIn"
        })

    state["strategies"] = strategies
    return state
