def maxProfit(prices) -> int:
    profit = 0
    left = 0
    for right in range(len(prices)):
        if prices[left] > prices[right]:  # find new min
            left = right
        else:
            # take max of highest recorded rise in prices
            profit = max(profit, prices[right] - prices[left])
    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]))

profit = 0
left = 0
right = 0
