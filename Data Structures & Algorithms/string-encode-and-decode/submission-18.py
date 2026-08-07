class Solution:
    """
    5#Hello5#World
      ^
    """

    def encode(self, strs: List[str]) -> str:
        encode_to_decode = ""
        for s in strs:
            encode_to_decode += str(len(s)) + "#" + s
        return encode_to_decode

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        """
        5#Hello5#World
        i
         j
        """
        while i < len(s):
            count = 0
            while s[j] != "#":
                j += 1
            count = int(s[i:j])
            res.append(s[j+1:j+1+count])
            j = j + 1 + count
            i = j
        return res



