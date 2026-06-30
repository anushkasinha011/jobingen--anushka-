from langgraph.graph import StateGraph, END

from agent.state import AgentState

from agent.nodes.trend_scout import trend_scout_node
from agent.nodes.signal_synthesizer import signal_synthesizer_node
from agent.nodes.trend_scorer import trend_scorer_node
from agent.nodes.audience_modeler import audience_modeler_node
from agent.nodes.platform_strategist import platform_strategist_node
from agent.nodes.angle_selector import angle_selector_node
from agent.nodes.copywriter import copywriter_node
from agent.nodes.visual_director import visual_director_node
from agent.nodes.analysis import analysis_node

from agent.state import AgentState

from agent.nodes.trend_scout import trend_scout_node
from agent.nodes.signal_synthesizer import signal_synthesizer_node
from agent.nodes.trend_scorer import trend_scorer_node
from agent.nodes.platform_strategist import platform_strategist_node
from agent.nodes.angle_selector import angle_selector_node
from agent.nodes.copywriter import copywriter_node
from agent.nodes.visual_director import visual_director_node
from agent.nodes.analysis import analysis_node


def build_graph():

    graph = StateGraph(AgentState)

    # Nodes
    graph.add_node("trend_scout", trend_scout_node)
    graph.add_node("signal_synthesizer", signal_synthesizer_node)
    graph.add_node("trend_scorer", trend_scorer_node)
    graph.add_node("platform_strategist", platform_strategist_node)
    graph.add_node("angle_selector", angle_selector_node)
    graph.add_node("copywriter", copywriter_node)
    graph.add_node("visual_director", visual_director_node)
    graph.add_node("analysis", analysis_node)
    graph.add_node("audience_modeler", audience_modeler_node)

    # Flow
    graph.set_entry_point("trend_scout")

    graph.add_edge("trend_scout", "signal_synthesizer")
    graph.add_edge("signal_synthesizer", "trend_scorer")
    graph.add_edge("trend_scorer", "audience_modeler")
    graph.add_edge("audience_modeler", "platform_strategist")
    graph.add_edge("platform_strategist", "angle_selector")
    graph.add_edge("angle_selector", "copywriter")
    graph.add_edge("copywriter", "visual_director")
    graph.add_edge("visual_director", "analysis")
    graph.add_edge("analysis", END)

    return graph.compile()

