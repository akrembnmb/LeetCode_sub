class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(arr,l,r):
            while l<r:
                arr[l], arr[r] = arr[r], arr[l]
                l+=1 
                r-=1
        k = k % len(nums)
        l, r = 0, len(nums)-1
        reverse(nums,l,r)
        l = 0
        r = k-1
        reverse(nums,l,r)
        l = k
        r = len(nums)-1
        reverse(nums,l,r)
        #O(n) Time
        #O(1) Space