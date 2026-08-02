class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mi = (r + l) // 2
            if nums[mi] < target: 
                l = mi + 1
            elif nums[mi] > target:
                r = mi - 1
            else:
                return mi

        return -1 
        

        """
        nums=[-1,0,2,4,6,8]
               l   mi    r
                    l r

        """
            