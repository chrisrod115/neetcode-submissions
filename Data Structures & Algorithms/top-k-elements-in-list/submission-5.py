class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        pairs = list(count.items())

        pairs.sort(reverse = True, key = lambda x:x[1])

        for i in range(k):
            res.append(pairs[i][0])
        return res