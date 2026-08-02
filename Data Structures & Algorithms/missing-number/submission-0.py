class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # [0, n] --> ok so any num from 0 -> n? 
        # like 0 -> 20? 
        # missing = 1
        # for i in range(len(nums)):
            
        #     if (nums[i] - (nums[i +1])) != missing: 
        #         # obv not return false but still thinking of
        #         # how to implement it
        #         return (nums[i] + (nums[i +1])) / 2
            # am i on the right track? 
            # why divide by 2 --> [1,2,4]
                              # --> 2 + 4 / 2 = 3

            # maybe easier, you can check that the current
            # number is the number you expect

            # the prompt says all numbers are in the range
            # 0 to n (NO DUPES AND ONLY ONE MISSING)
            # so what if you just check the number you
            # expect to see

            # example:
            # nums = [0,1,2,3,4,6]
            #                 x
            # i expect to see 2 i think i got it lmaooo 
            # that makes so much more sense
        # if the num is the next num right? like if its

        # define the first number you expect to see
        # as a variable
        a = 0

        # sort nums
        nums.sort()
        
        # iterate over nums
        for i in range(len(nums)):
            # if this number is not what i expect to see
            # it's a, not 0
            # you return the missing number so rtn a
            if nums[i] != a:
                return a 
            # else, increment the expected number
            else:
                a += 1

        # so return a here
        return a
        # since we are guaranteed that a number is missing, it could
        # be the last number

        # consider
        # nums = [0,1,2] so 3 is missing

        # but this algorithm only works if nums is ___________
        