class Solution:

    def encode(self, strs: List[str]) -> str:
        # Input: strs = ["Hello","World"]
        # 5#Hello5#World10#christophe
        #               ^
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string
    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World
        # i
        #        j
        res = []
        i = 0
        j = 0
        while i < len(s):
            count = 0
            while s[j] != "#":
                j += 1
            count = int(s[i:j])
            res.append(s[j+1:j+1+count])
            j = j + 1 + count
            i = j
        return res


            
            
        

