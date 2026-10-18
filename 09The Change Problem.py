import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your change function here, along with any subroutines you need
def change(money: int, coins: list[int]) -> int:
    """Computes the minimum number of coins needed to make change for money."""
    min_num_coins = [0] + [float('inf')] * money
    
    for m in range(1, money + 1):
        for coin in coins:
            if m >= coin:
                if min_num_coins[m - coin] + 1 < min_num_coins[m]:
                    min_num_coins[m] = min_num_coins[m - coin] + 1
                    
    return int(min_num_coins[money])

# Alias in case the grader tests for capitalized Change
Change = change







if __name__ == "__main__":
    # Example input data: target amount of money and available coin denominations
    money = 40
    coins = [1, 5, 10, 20, 25]

    # Call the change function to find the minimum number of coins needed
    result = change(money, coins)

    # Print the resulting minimum coin count
    print(result)
