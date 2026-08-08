class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for n in nums:
            if (n - 1) not in nums:
                local_count = 0
                while (n + local_count) in nums:
                    local_count += 1
                res = max(res, local_count)

        return res