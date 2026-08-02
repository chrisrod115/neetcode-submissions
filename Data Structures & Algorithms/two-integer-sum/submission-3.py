class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in h_map:
                # 7 - 4 = 3 --> h_map= {value, index}
                #                    = {3: 0,}
                #               h_map[3] --> 0 index
                #               i --> current index of 4
                return [h_map[diff], i]
            h_map[n] = i
        
            