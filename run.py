from agent.graph import build_graph
from agent.state import AgentState

if __name__ == "__main__":

    app = build_graph()

    initial_state = AgentState()

    final_state = app.invoke(initial_state)

    print("\n========== SCORED TRENDS ==========\n")

    for trend in final_state.get("scored_trends", []):
        print(f"{trend['topic']} : {trend['score']}")

    print("\n========== COPY ==========\n")

    for post in final_state.get("copy", []):
        print(post)

    print("\n========== VISUALS ==========\n")

    for visual in final_state.get("visuals", []):
        print(visual)

    if final_state.get("errors"):
        print("\n========== ERRORS ==========\n")
        for err in final_state["errors"]:
            print(err)