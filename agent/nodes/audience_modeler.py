def audience_modeler_node(state):
    audience = []

    for trend in state.get("scored_trends", []):
        audience.append({
            "topic": trend["topic"],
            "audience": "Students, Developers, Job Seekers",
            "pain_points": [
                "Learning AI",
                "Career Growth",
                "Finding Jobs"
            ],
            "interest_score": trend["score"]
        })

    state["audience"] = audience
    return state