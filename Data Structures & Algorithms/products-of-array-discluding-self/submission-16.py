class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Input: nums = [1,2,4,6]
        product left + product right
        pre = 1
            = 1
            = 2
            = 8
        [1,1,2,8]
        post = 1
        [1,1,2,8]
        post = 6
        [1,1,12,8]
        post = 24
        [1,24,12,8]
        post = 2 * 24
        """
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

