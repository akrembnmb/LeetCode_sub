class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        
        count_0 = nums.count(0)
        count_1 = count_0 + nums.count(1)
        count_2 = count_1 + nums.count(2)
        
        index = 0
        while index < len(nums):
            if index < count_0:
                nums[index] = 0
            elif index < count_1:
                nums[index] = 1
            elif index < count_2:
                nums[index] = 2
            index += 1
        
        return nums
#O(n)