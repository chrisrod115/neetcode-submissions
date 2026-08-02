class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            s_len = str(len(s))
            res += s_len + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        while i < len(s):
            while s[j] != "#":
                j += 1
            count = int(s[i:j])
            res.append(s[j+1:j+count+1])
            j += 1 + count
            i = j
        return res