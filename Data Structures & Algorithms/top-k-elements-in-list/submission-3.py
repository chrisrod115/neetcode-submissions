class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            res[nums[i]] = 1 + res.get(nums[i], 0)
        # Current position --> {1:1, 2:2, 3:3} {num:count}
        pairs = list(res.items())
        # Current position --> [(1,1), (2,2), (3,3)]
        # def func(x): return x[1]
        pairs.sort(key = lambda x: x[1], reverse = True)

        # return top K up to K
        top_k = []
        for i in range(k):
            top_k.append(pairs[i][0])
        return top_k


        