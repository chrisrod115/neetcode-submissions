class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, res = 0, len(heights)-1, 0
        while l < r:
            area = (min(heights[l],heights[r]) * abs(r - l))
            res = max(res, area)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res