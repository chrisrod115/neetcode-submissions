class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Go through the list of numbers in the nums array
        2 --> check if there is a 1 if not continue>>>>
        if there is a 3 then add on to a counter and continue
        return max(res, current count)

        """

        res = 0
        nums = set(nums)
        for n in nums:
            if (n-1) in nums:
                continue
            cur = 1
            while (n+1) in nums:
                cur += 1
                n += 1
            res =  max(res, cur)
        return res
                