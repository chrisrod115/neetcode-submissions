class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs = ["act","pots","tops","cat","stops","hat"]
        #          "act"
        #           p
        # --> add count to h_map --> 
        #h_map = {
        #        key:                                                           value
        #        (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0):         [""]
        #        (1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0):         ["act", "cat"]
        #                       
        #        }

        # loop through strings --> creating an o(n)
        # loop through characters adding them to a h_map --> o(m) time 
        # same space complexity --> o(n) * o(m) --> o(n * m)

        h_map = defaultdict(list)

        for s in strs: 
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            h_map[tuple(count)].append(s)
        return h_map.values()