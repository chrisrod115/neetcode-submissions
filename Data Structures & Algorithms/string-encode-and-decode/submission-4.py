class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: 
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        #this is the part i get confused about IG figuring out how to decode the str
        # s = "1#i4#love10#leetcoding"
        #               i    j
        # just need to repeat the following:
        #   - read number up until a hashtag (count)
        #   - append the next [count] characters to your list
        # if u mean confused in terms of writing code, just use 2 pointers, say i and j
        # i will serve as the starting point of the number (points at the first digit in [count])
        # j will serve as the ending point of the number (points at the hashtag)
        # ok I think i got it
        res = []

        # Declare pointer i and j here
        # start them bothat 0
        i, j = 0, 0

        # while i does not go out of bounds
        while i < len(s):
            # make j go forward until it reaches a hashtag
            while s[j] != "#":
                j += 1

            # get the count by looking at the characters from i to j (exclusive since we don't include the hashtag)
            count = int(s[i:j])

            # the next *count* characters after j (j is currently pointing to a #) should be appended to res
            # you could use a loop but 1) the bounds need to be edited, 2) can just use basic math
            # if i want the next *count* characters after j, i look at j + 1 until j + 1 + count ahhhh lmao true and that 
            res.append(s[j+1:j+1+count])
            i = j + 1 + count 
            j = i

        return res
         

