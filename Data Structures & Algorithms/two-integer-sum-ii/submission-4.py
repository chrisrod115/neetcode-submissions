class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non-decending order --> basically means sorted: 
        # numbers = [1,2,3,4], target = 3
        # target = 3 --> 4 - 1 = 3 --> [0,3]
        # binary search: 
        # basically two pointers and check if the result if less that or greater than
        # numbers = [1,2,3,4], target = 3
        #            L
        #                  R
        # if the sum of left and right > 3 --> 1 + 4 = 5 > 3 move right left 
        # if the sum of left and right < 3 --> 1 + 1 = 2 < 3 move left right 
        # else return index of left and right in a list
        left, right = 0, len(numbers) - 1
        while left < right: 
            if (numbers[left] + numbers[right]) > target: 
                right -= 1
            elif (numbers[left] + numbers[right]) < target: 
                left += 1
            else:
                return [left+1, right+1]
