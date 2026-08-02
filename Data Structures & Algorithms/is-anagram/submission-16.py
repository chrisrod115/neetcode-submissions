class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        
        s_cnt = {}
        t_cnt = {}

        for i in range(s_len):
            s_cnt[s[i]] = 1 + s_cnt.get(s[i], 0)
            t_cnt[t[i]] = 1 + t_cnt.get(t[i], 0)
        
        return s_cnt == t_cnt