class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_count = {}
        for n in nums:
            if n in freq_count:
                return True
            freq_count[n] = 1
        return False