class Solution:

    def encode(self, strs: List[str]) -> str:
        e_str = ""
        for s in strs:
            e_str += str(len(s)) + "#" + s
        return e_str

    def decode(self, s: str) -> List[str]:
        # Create a result list:
        res = []
        # Create two pointers i and j initialize them to zero
        i, j = 0, 0

        # Now you need to move the pointers accordingly
        # s = "1#i4#love10#leetcoding"
        #      i
        #      j
        # Loop through the string till we get to the end
        while i < len(s):
        # the way to move this is to increment j --> to "#" 
        # delimeter
            while s[j] != "#":
                j += 1
            # Now that we hit the delimeter the len is between i and j
            # add that number to the count var
            count = int(s[i:j])
            # Now we have this: 
            # s = "1#i4#love10#leetcoding"
            #        i
            #         j
            # count = 1 --> therefore, move j + 1
            j = j + 1
            i = j
            j = j + count
            res.append(s[i:j])
            i = j

        return res


