class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        [1] [2] [2] [3] [3] [3]

        [0] [1] [2] [3] [4] [5] [6]

             1   2   3

        [] [1] [2] [3] [] [] []

        
        """

        freq_bucket = [[] for i in range(len(nums) + 1)]
        
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        for n, f in counter.items():
            freq_bucket[f].append(n)
        
        res = []
        """
        freq_bucket = [[], [1], [2], [3]]
        freq[0] = empty
        freq[1] = 1
        """
        for i in range(len(freq_bucket) - 1, -1, -1):
            for n in freq_bucket[i]:
                res.append(n)
                if (len(res) == k):
                    return res

            

        