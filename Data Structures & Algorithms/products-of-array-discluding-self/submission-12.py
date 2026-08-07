class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            # print(f"res{i}: {res[i]}")
            prefix *= nums[i]
            # print(f"i = {i}, prefix: {prefix}")
        """
        
        nums = [1,2,4,6]
        prefix = 1
        res = [1,1,1,1]
        res = [1,1,2, 8]

        res = 
        prefix * nums[i]


        """
        post = 1
        for i in range(len(nums)-1, -1 , -1):
            res[i] *= post
            post *= nums[i]
        return res