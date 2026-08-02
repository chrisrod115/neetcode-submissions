class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s = "zxyzxyz"
        #        L
        #           R
        # seen = {"z", "x"}

        # s = "abcdb"
        #        L
        #            R
        #  res = 4
        # seen = {"c", "d", "b"}

        # res = 0
        # seen = set()
        # left = right = 0
        # while right < len(s):
        #     while s[right] in seen:
        #         seen.remove(s[left])
        #         left += 1
            
        #     res = max(res, right - left + 1)
        #     seen.add(s[right])
        #     right += 1
        # return res

        res = left = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            res = max(res, right - left + 1)
            seen.add(s[right])
        return res