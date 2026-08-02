class Solution:
    def isPalindrome(self, s: str) -> bool:
        #  s = "4Was it a car or a cat I saw4?"
        #         L                       R
        # s = ".,"
        #       L
        #      R
        left, right = 0, len(s) - 1
        while left < right:
            while (left < right) and not(s[left].isalnum()):
                left += 1
            while (left < right) and not(s[right].isalnum()):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            # update left and right
            left, right = left + 1, right - 1
        return True
