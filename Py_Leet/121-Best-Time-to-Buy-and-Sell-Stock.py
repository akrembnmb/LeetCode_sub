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
       