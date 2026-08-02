class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers = [1,2,3,4], target = 3
        seen = {}
        # for i in range(len(numbers)):
        #     diff = target - numbers[i]
        #     if diff in seen:
        #         # diff = 2
        #         # numbers[i] = 1
        #         # (1, 2, 3, 4)
        #         return [diff]
        #     seen.add(numbers[i])
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in seen:
                # seen = {1: 0, 2: 1, 3: 2, 4: 3}
                return[seen[diff] + 1, i + 1]
            seen[n] = i