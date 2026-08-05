class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Input: nums = [1,2,4,6]
                       ^     ^
        Output: [48,24,12,8]

        

        


         0 1 2 3
        [1,1,1,1]
        [1,2,4,6]

        res[i] 0  = 1
        res[1] = 1
        res[2] = 2
        res[3] = 8 


        postfix = 1
        res = [1,1,2,8]
        res[3] *= postfix
        postfix *= nums[i]
        """
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(res) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return(res)
