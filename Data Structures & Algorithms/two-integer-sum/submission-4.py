class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            # [3, 4, 5, 6] target = 7
            #  i
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i