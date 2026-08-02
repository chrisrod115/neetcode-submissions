class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        """
        [1,1,1,1]
             ^ 
        [1,2,4,6]
             ^
        [1,1,2,8]
        [48,24,12,8]
        """

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res
            