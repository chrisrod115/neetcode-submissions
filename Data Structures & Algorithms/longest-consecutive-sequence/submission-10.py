class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Input: nums = [2,20,4,10,3,4,5]
        #                   i
        # 2 -> 3 -> 4 ->5
        res = 0
        nums = set(nums)
        for n in nums:
            if ((n-1) not in nums):
                local_count = 1 
                while ((n+1) in nums):
                    local_count += 1
                    n += 1
                res = max(local_count, res)
        return res
