class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hist = {}
        for i in range ( len(nums)) :
            if target - nums[i] in hist:
               return [i,hist[target - nums[i]]]
            else : hist[nums[i]] = i
            #O(n)