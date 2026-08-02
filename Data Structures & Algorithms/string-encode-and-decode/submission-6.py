class Solution:

    def encode(self, strs: List[str]) -> str:

        new_s = ""
        for s in strs:
            new_s += str(len(s)) + "#" + s
        return new_s 

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0

        while i < len(s):
            while s[j] != "#":
                j += 1
            count = int(s[i:j])
            res.append(s[j+1:j+1+count])
            i = j + 1 + count 
            j = i
        
        return res
