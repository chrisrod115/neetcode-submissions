class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, res = 0, len(heights) - 1, 0
        while l < r:
            area = (min(heights[l], heights[r])) * abs(l - r)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            res = max(area, res)
        return (res)
            