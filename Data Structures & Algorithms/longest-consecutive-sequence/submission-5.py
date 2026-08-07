class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Input: nums = [2,20,4,10,3,4,5]
        longest = 2, 3, 4, 5 = 4
        20 doesn't have a consecutive length 
        10 doesn't have a consecutive length
        return longest
        set(nums) <- only unique values
        """
        nums = set(nums)
        longest = 0
        for n in nums:
            """
            Here we are checking if n - 1 is not in our set which will make it a head:
            i.e nums = [2,20,4,10,3,4,5]
            iteration 1: n = 2
            does n - 1 exist in the set? 2 - 1 = 1 --> no 1 doesn't exist
            """
            if (n-1) not in nums: 
                """
                Here we are checking the inner longest so we just pass through the array once.
                i.e nums = [2,20,4,10,3,4,5]
                does n + 0 exist in our set()? 
                n == 2 + 0 ==> 2 yes 
                current = 0 + 1 = 1
                n == 2 + 1 = 3 in set? yes
                keep going till n + 1 not in nums
                """
                current = 0
                while (n + current) in nums:
                    current += 1
                """
                Finally take the maximum and store it in longest
                and do this for each head sequence. The n - 1 check automatically 
                skips what has already been checked.
                Don't believe me! watch this: n == 3 --> alright bet!
                Logic (n - 1 not in set?) --> (3 - 1 == 2) oh whaaa 2 in set bruh skip that!
                """
                longest = max(current, longest)
                
        return longest
