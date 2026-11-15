class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count_s = {}
        char_count_t = {}

        for i in range(len(s)):
            char_count_s[s[i]] = 1 + char_count_s.get(s[i], 0)
            char_count_t[t[i]] = 1 + char_count_t.get(t[i], 0)
        
        return char_count_s == char_count_t