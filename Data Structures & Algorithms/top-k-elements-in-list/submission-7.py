class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the occurances of each number in nums
        h_map = {}
        for n in nums:
            h_map[n] = 1 + h_map.get(n, 0)
        
        # Create a list of pairs so that we can sort through them by (n, count) count.
        pairs = list(h_map.items())
        pairs.sort(key = lambda x:x[1], reverse = True)

        # Return the result in a list (n, count) --> return [n, n + 1 ....] up to k
        res = []
        for i in range(k): 
            res.append(pairs[i][0])
        return res