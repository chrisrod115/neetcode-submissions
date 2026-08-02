class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        while i < len(s):
            while s[j] != "#":
                j += 1
            count = int(s[i:j])
            # Ex. "4#team2#to3#sum"
            #            i
            #            j
            res.append(s[j+1:j+1+count])
            j = j + 1 + count
            i = j
        return res

