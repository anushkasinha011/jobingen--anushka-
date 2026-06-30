def angle_selector_node(state):

    angles = []

    for trend in state.get("scored_trends", []):

        angles.append({
            "topic": trend["topic"],
            "angle": "Educational"
        })

    state["angles"] = angles
    return state