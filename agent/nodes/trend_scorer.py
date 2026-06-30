def trend_scorer_node(state):
    scored = []

    for signal in state.get("signals", []):
        score = signal["score"] * 10

        scored.append({
            "topic": signal["topic"],
            "score": score
        })

    state["scored_trends"] = scored
    return state