class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Input: nums = [-1,0,2,4,6,8], target = 4
        for i, n in enumerate(nums):
            if n != target:
                continue
            else:
                return i
        return -1