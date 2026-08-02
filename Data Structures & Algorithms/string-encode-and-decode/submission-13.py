class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            s_len = str(len(s))
            res += s_len + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        res = []
        while i < len(s):
            # 4#neet4#code4#love3#you
            #  i
            #  j
            while (s[j] != '#'):
                j += 1
            count = int(s[i:j])
            i = j
            res.append(s[i + 1:j + count + 1])
            j += 1 + count
            i = j
        return res