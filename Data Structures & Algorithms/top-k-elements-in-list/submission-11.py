class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort
        
        # Count occurrences of each n in nums
        count = {}  # Space: O(n)
        freq = [[] for i in range(len(nums) + 1)]  # Space: O(n)
        
        # Create the count hash map
        for n in nums:  # Time: O(n)
            count[n] = 1 + count.get(n, 0)  # Time: O(1) on average, since dictionary operations are O(1)

        # Populate the frequency buckets
        for n, c in count.items():  # Time: O(n)
            freq[c].append(n)  # Time: O(1)
            print(freq)

        # Collect the top k frequent elements
        res = []  # Space: O(k)
        for i in range(len(freq) - 1, 0, -1):  # Time: O(n)
            for n in freq[i]:  # O(1) time
                res.append(n)  # Time: O(1)
                if len(res) == k:  # Time: O(1)
                    return res  # Time: O(1)

        # Time: O(n + n + 1 + n + 1 + 1 + 1 + 1) --> res O(n)
        # Space: O(n + n + k) --> k is used in the return --> res O(n) 