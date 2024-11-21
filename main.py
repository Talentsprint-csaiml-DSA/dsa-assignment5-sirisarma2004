def min_coins(coins, target_amount):
  dp = [float("inf") for i in range(target_amount + 1)]
  dp[0] = 0
  for coin in coins:
    count = coin
    while (count <= target_amount):
      if dp[count] > dp[count - coin] + 1:
        dp[count] = dp[count - coin] + 1
      count += 1
  return dp.pop()