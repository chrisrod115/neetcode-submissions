class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for num in nums: 
            count[num] = 1 + count.get(num, 0)
        pairs = list(count.items())
        pairs.sort(key = lambda x:x[1], reverse = True)
        
        for i in range(k):
            res.append(pairs[i][0])
        return res