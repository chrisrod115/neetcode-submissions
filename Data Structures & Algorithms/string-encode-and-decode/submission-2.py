class Solution:
    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for s in strs:
            new_str += str(len(s)) + "#" + s
        return new_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = j = 0
        while j < len(s):
            while s[j] != "#":
                j += 1
            
            cnt = int(s[i:j])
            res.append(s[j + 1:j + 1 + cnt])
            j = j + 1 + cnt
            i = j
        return res

# Example 1
# ["n3()3t","6cod@e","l#$4ve","u4$"]
#       Encode
#       "6#n3()3t216#6cod@e5#l#$4ve3#u4$"

# Example 2
# ["neet","code","love","you"]
#       Encode
#         "4neet4code4love3you"  