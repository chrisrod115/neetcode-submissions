class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map = {}
        top_k = []
        for i in range(len(nums)):
            h_map[nums[i]] = 1 + h_map.get(nums[i], 0)
        # h_map = {1:1, 2:2, 3:3}

        # Convert to list of pairs
        pairs = list(h_map.items())

        # Sort
        pairs.sort(key = lambda x: x[1], reverse = True)

        # Return the top k
        for k_val in range(k):
            top_k.append(pairs[k_val][0])
        return top_k
