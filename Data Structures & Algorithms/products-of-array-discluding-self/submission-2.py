class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
            # nums = [1,2,4,6]
        count = 1
        for i in range(len(nums) - 1, -1, -1):
            # res = [1,1,2,8] 8
            res[i] *= count
            count *= nums[i]

        return res