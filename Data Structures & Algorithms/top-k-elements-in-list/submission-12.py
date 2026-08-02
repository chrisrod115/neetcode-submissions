class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_count = {}
        for n in nums:
            f_count[n] = 1 + f_count.get(n, 0)

        pairs = list(f_count.items())

        pairs.sort(key = lambda x: x[1], reverse = True)

        res = []
        for i in range(k):
            res.append(pairs[i][0])
        return res