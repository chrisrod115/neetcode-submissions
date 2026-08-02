class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            width = (r - l) # use the left and right pointers on the horizontal axis to get width value
            height = min(heights[l], heights[r]) # only use the smallest height to get the area, because of overflow
            area = width * height
            res = max(res, area)

            if heights[l] < heights[r]:
                l+=1
            elif heights[r] <= heights[l]:
                r-=1
        return res