class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         h_set = set()
         for n in nums: 
            if n in h_set:
                return True
            h_set.add(n)
         return False