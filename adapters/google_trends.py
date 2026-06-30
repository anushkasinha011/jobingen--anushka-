def get_google_trends():
    """
    Mock trending topics until a stable trends source is integrated.
    """
    return [
        "Artificial Intelligence",
        "ChatGPT",
        "Python",
        "Marketing Automation",
        "AI Agents"
    ]


if __name__ == "__main__":
    print(get_google_trends())
