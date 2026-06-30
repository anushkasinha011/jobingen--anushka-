from typing import TypedDict, List, Dict, Any


class AgentState(TypedDict, total=False):
    trends: List[str]
    news: List[Dict[str, Any]]
    reddit: List[Dict[str, Any]]

    signals: List[Dict[str, Any]]
    scored_trends: List[Dict[str, Any]]

    strategies: List[Dict[str, Any]]
    angles: List[Dict[str, Any]]
    copies: List[Dict[str, Any]]
    visuals: List[Dict[str, Any]]

    analysis: Dict[str, Any]

    errors: List[str]