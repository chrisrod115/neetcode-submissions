class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
                0 1 2 3 4 5
        nums = [3,4,5,6,1,2]
                      l
                        m
                      r
        """
        res = float("inf")
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            res = min(res, nums[mi])
            if nums[mi] > nums[hi]:
                lo = mi + 1
            else:
                hi = mi - 1
        return res