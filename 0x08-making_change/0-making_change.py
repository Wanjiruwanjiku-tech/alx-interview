#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed to meet a given total
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    
    Args:
        coins (list): The list of coin denominations available.
        total (int): The target amount.
    
    Returns:
        int: Fewest number of coins needed to meet total, or -1 if not possible.
    """
    if total <= 0:
        return 0
    
    coins.sort(reverse=True)  # Sort coins in descending order for greedy approach
    num_coins = 0
    for coin in coins:
        if total == 0:
            break
        # Use as many of this coin as possible
        num_coins += total // coin
        total %= coin
    
    # If after all operations, total is not 0, it means we cannot make the change
    return num_coins if total == 0 else -1
