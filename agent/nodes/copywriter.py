def copywriter_node(state):

    copies = []

    for strategy in state.get("strategies", []):

        copies.append({
            "topic": strategy["topic"],
            "caption": f"Latest update on {strategy['topic']}."
        })

    state["copies"] = copies
    return state