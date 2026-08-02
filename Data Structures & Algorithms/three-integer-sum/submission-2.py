class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        a + b + c = 0
        _ + _ + _ = 0
        set a to the first value and use the two pointer method to solve the rest
        go through all the possible combinations for that one value.

        Input: nums = [-1,0,1,2,-1,-4]
                        n
        l = 0, n = -1
        r = 5, n = -4

        """
        res = []
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = n + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res

                