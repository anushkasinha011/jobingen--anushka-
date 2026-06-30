def visual_director_node(state):

    visuals = []

    for copy in state.get("copies", []):

        visuals.append({
            "topic": copy["topic"],
            "image_prompt": f"Modern marketing graphic about {copy['topic']}"
        })

    state["visuals"] = visuals
    return state