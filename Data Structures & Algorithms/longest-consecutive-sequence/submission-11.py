class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for n in nums:
            if (n - 1) not in nums:
                length_counter = 1
                while (n + 1) in nums:
                    length_counter += 1
                    n += 1
                res = max(res, length_counter)
        return res