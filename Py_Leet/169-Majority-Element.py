class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)/2
        d = {}
        for e in nums:
            if e in d:
                d[e]+=1
                if d[e]> n:
                    return int(e)
            else:
                d[e] = 1
                if len(d)==1 and d[e]> n:
                    return int(e)
                
                #O(n)
        