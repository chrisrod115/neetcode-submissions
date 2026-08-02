class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        """
        count[key] = value
        count = {
            1: 1,
            2: 2,..
        }
        pair = [(1,1), (2,2)]
        """
        pairs = list(count.items())
        pairs.sort(key = lambda x:x[1], reverse = True)
        
        res = []
        for i in range(k):
            res.append(pairs[i][0])
        return res