class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest=prices[0]
        for e in prices:
            if e<lowest : 
                lowest = e
            res = max(res,e-lowest)
        return res
        #O(n)
        # 2 Pointers
        """l , r = 0,1
        maxP = 0
        while r < len (prices) and l<r :
            if prices[l] < prices[r] :
                profit = prices[r] - prices[l] 
                maxP = max(maxP ,profit )
            else :
                l=r
            r+=1
        return maxP
        #O(n)"""
