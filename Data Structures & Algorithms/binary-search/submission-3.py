import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Input: nums = [-1,0,2,4,6,8], target = 4
        i = bisect.bisect_left(nums, target)
        if i < len(nums) and nums[i] == target:
            return i
        return -1