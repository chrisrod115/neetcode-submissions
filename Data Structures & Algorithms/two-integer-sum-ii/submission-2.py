class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # binary search
        # numbers = [1,2,3,4], target = 3
        # since nums are sorted: 
        
        # numbers = [1,2,3,4], target = 3
        #            L     R
        # if sum of L and R is target return index of L & R
        # if left is lower is than right
        # if left is lower is higher right
        # this will have O(1) space complexity
        left, right = 0, len(numbers) - 1
        while left < right: 
            current_sum = numbers[left] + numbers[right]
            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                return [left+1, right+1]

        