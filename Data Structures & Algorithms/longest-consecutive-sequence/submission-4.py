class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # o(n) space
        longest = 0 
        for n in nums: # o(n) time
            # check if it's the start of a sequence
            if (n - 1) not in numSet: # o(1)
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest