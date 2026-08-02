class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dup = {}
        for i, n in enumerate(nums): 
            diff = target - n
            if diff in dup:
                return [dup[diff], i]
            dup[n] = i
