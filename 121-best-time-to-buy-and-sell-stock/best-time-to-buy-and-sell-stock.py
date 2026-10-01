class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minv = prices[0]
        for num in prices:
            minv = min(minv,num)
            maxp = max(maxp,num-minv)
        return maxp
        
        