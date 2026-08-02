class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, v in enumerate(nums):
            diff = target - nums[i]
            if diff in res:
                return [res[diff], i]
            res[v] = i
        return False