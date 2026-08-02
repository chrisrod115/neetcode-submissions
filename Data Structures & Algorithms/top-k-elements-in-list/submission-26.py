class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        # [[0], [1], [2], [3], [4], [5], [6]]
        # [7, 7] k = 1
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        
        for n, f in count.items():
            buckets[f].append(n)
        
        res = []

        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                res.append(n)
                if (len(res) is k):
                    return res

