class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums: 
            count[n] = 1 + count.get(n, 0)

        """
        nums = [1,2,2,3,3,3]
        count = {
            1: 1,
            2: 2,
            3: 3,
        }
        freq = [[],[],[],[],[],[],[]] list of lists of size 7 --> need 7 bc we need to have a zero index
        indicies:0. 1. 2. 3. 4. 5. 6

        fill the buckets by addeding the number of occurances to each bucket
        therefore, it should look like this: freq = [[],[1],[],[],[],[],[]] <-- freq[1].append(1) 
                                                      0  1  2  3  4  5  6          
        therefore, it should look like this: freq = [[],[1],[2],[],[],[],[]] <-- freq[2].append(2)
                                                      0  1   2  3  4  5  6          
        therefore, it should look like this: freq = [[],[1],[2],[3],[],[],[]] <-- freq[3].append(3)
                                                      0  1   2   3  4  5  6          
        """
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
