class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        s_len = len(s)
        i, j = 0, 0

        while i < s_len:
            # 4#neet4#code4#love3#you
            # ^                   
            #       ^               
            while s[j] != "#":
                j += 1
            count = int(s[i:j])
            # j + 1 : 0 + 1 + 4 = 5 <-- not inclusive
            res.append(s[j + 1: j + 1 + count])
            j = j + 1 + count
            i = j 
        return res