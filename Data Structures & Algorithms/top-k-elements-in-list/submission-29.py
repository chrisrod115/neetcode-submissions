class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Input: nums = [1,2,2,3,3,3], k = 2

        """
        bucket = [[] for i in range(len(nums) + 1)]
        count = {}

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        
        for v, f in count.items():
            bucket[f].append(v)

        res = []
        print(bucket[1])
        for i in range(len(bucket) - 1, -1 , -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
