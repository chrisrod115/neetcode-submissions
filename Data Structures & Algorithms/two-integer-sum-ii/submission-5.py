class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0, len(numbers) - 1

        while left < right:
            if (numbers[left] + numbers[right]) > target:
                # 1 + 4 = 5 --> target = 3 greater therefor lower right
                right -= 1

            elif (numbers[left] + numbers[right]) < target:
                # 1 + 4 = 5 --> target = 3 greater therefor lower right
                left += 1
            
            else:
                return [left + 1, right + 1]
            