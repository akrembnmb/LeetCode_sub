class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for e in nums:
            if not e-1 in numset:
                l = 0
                while e+l in numset:
                    l+=1
                longest = max(longest,l)
        return longest
        #O(n)
                