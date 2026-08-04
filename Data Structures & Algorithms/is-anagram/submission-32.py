class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len, t_len , s_count, t_count = len(s), len(t), {}, {}
        if s_len != t_len:
            return False
        
        for i in range(s_len):
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)
        
        return s_count == t_count