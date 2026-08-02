class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,2,2,3,3,3], k = 2
        #           2   3 --> most freq --> returns: [2,3]
        # h_map = {key: value} --> {}
        # most freq occurance counter 
        h_map = {}
        most_freq = []
        for i in range(len(nums)):
            h_map[nums[i]] = 1 + h_map.get(nums[i], 0)
            # [1,2,2,3,3,3]
            # {1: 1; 2: 2; 3: 3}

        pairs = list(h_map.items())
        print(pairs)
        # pairs = [(1, 1), (2, 2), (3, 3)]
        # x = (1, 1)
        pairs.sort(key=lambda x: x[1], reverse=True)
        print(pairs)
        # Python dictionaries
        # h_map = {
        #       1: 4,
        #       2: 5,
        #       3: 3 
        # }

        #   keys: [1,2,3]
        # values: [4,5,3]

        # Sorted
        #   keys: [3,1,2]
        # values: [3,4,5]

        for key in range(k):
            print(key)
            most_freq.append(pairs[key][0])
        return most_freq
