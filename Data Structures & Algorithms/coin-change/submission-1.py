class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {} # amount: min_coins

        def recursion(amount):
            if amount == 0: # 2. Write the boundary conditions
                return 0
            if amount < 0:
                return float('inf')
            if amount in dp:
                return dp[amount]

            min_coins = float('inf') # 3. Then write the recursion logic
            for coin in coins:
                count = recursion(amount-coin)
                min_coins = min(count+1, min_coins)
                dp[amount] = min_coins

            return min_coins # 1. Write the return statement first

        min_coins = recursion(amount)
        return min_coins if min_coins != float('inf') else -1