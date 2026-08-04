class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        nums = [1,2,2,3,3,3], k = 2
        1: 1, 3: 3, 2: 2
        1: 1, 2: 2, 3: 3
        """
        bucket = [[] for i in range(len(nums) + 1)]
        
        counter = {}
        for i in range(len(nums)):
            counter[nums[i]] = 1 + counter.get(nums[i], 0)
        
        for n, f in counter.items():
            bucket[f].append(n)

        result = []

        for i in range(len(bucket) - 1, -1, -1):
            for n in bucket[i]:
                result.append(n)
                if len(result) == k:
                    return result
                
