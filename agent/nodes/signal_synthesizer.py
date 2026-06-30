def signal_synthesizer_node(state):
    signals = []

    for trend in state.get("trends", []):
        signals.append({
            "topic": trend,
            "score": 1
        })

    state["signals"] = signals
    return state