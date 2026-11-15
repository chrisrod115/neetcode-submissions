class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        nums = [1,2,2,3,3,3], k = 2

        """

        top_k = [[] for i in range(len(nums) + 1)]
        
        k_count = {}

        for i, v in enumerate(nums):
             k_count[v] = 1 + k_count.get(v, 0)
        
        for num, frequency in k_count.items():
            top_k[frequency].append(num)
        
        res = []
        
        for i in range(len(top_k) -1, -1, -1):
            for top in top_k[i]:
                res.append(top)
                if (len(res)) == k:
                    return res