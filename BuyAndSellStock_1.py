class Solution:
  # @param prices, a list of integer
  # @return an integer
  def maxProfit(self, prices):
    length = len(prices)
    if (length < 1):
      return 0
    b = [0]
    c = 0
    pmin = prices[0]
    pmax = prices[0]
    bestmin = pmin
    bestmax = pmax
    trend = 0
    maxreturn = bestmax - bestmin

    for i in range(1, length):
      if (prices[i] > prices[i - 1]):
        if (trend < 0):
          pmax = prices[i]
        if (trend  >= 0):
          pmax = prices[i]
        trend = 1

      if (prices[i] < prices[i - 1]):

        if (trend > 0):
          returns = pmax - pmin
          if (returns > maxreturn):
            maxreturn = returns
            bestmax = pmax
            bestmin = pmin
        if (prices[i] < pmin):
          pmin = prices[i]
        trend = -1;
    returns = prices[length - 1] - pmin;
    if (returns > maxreturn):
      maxreturn = returns
    return maxreturn
