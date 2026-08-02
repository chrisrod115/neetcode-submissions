class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums = [1, 2, 3, 3]
        #         i  j
        # set() --> different from "() <-- this is immutable" --> set() this version is not
        h_set = set()
        for n in nums:
            if n in h_set:
                return True
            h_set.add(n)
        return False
            