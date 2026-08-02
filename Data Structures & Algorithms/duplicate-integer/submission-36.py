class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_array = []
        for n in nums:
            if n in new_array:
                return True
            new_array.append(n)
        return False