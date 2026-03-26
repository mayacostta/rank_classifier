def classify_rank(wins: int, losses: int) -> str:
    """Classify a player based on the number of wins and losses."""
    ranks = ["Iron", "Bronze", "Silver", "Gold",
              "Diamond", "Legendary", "Imortal"]
    average_result = wins - losses
    index = average_result // 10
    if index >= len(ranks):
        index = len(ranks) - 1
    
    return f"You are on the {ranks[index]} rank!"


