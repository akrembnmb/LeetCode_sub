class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l , r = 0 , len(height)-1
        while l<r:
            ar = (r - l)* min(height[l],height[r])
            res = max(res,ar)
            if height[l] < height[r]:
                l+=1
            else : r-=1
        return res
#O(n) Time
#O(1) Memory
