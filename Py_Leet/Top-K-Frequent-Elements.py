class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d={}
        
        for e in nums:
            if e in d:
                d[e]+=1
            else:d[e]=1
        res = sorted(d, key=d.get, reverse=True)[:k]
            
        return res
""" Time complexity : O(nlogn)
    Memory complexity : O(n) """