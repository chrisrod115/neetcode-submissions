class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        """
        [1,2,2,3,3,3], k = 2
        [[1], [2,2], [3,3,3]] <-- not storing the numbers but the count of each occurance

        """
        for n in nums: 
            count[n] = 1 + count.get(n, 0)

        for n, f in count.items():
            freq[f].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res