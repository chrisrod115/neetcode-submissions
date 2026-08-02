class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        [2,20,4,10,3,4,5] --> index 1
        2 --> 3
        20 --> 21
        4 --> 5

        {2,20,4,10,3,4,5}
              n
        [2, ]
        [20, ...]
        [4] X -> because 3 in set
        [10, ...]
        [3] X -> because 2 in set
        [5] X -> because 4 in set

        count of len of sequence
        """
        res = 0
        nums = set(nums)
        for n in nums:
            if (n - 1) in nums:
                continue

            cur = 1
            while (n + 1) in nums:
                cur += 1
                n += 1
            res = max(res, cur)
        return res