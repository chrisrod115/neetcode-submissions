class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;

        unordered_map<char, int> s_count;
        unordered_map<char, int> t_count;

        for (auto c: s) {
            s_count[c]++;
        }

        for (auto c: t) {
            t_count[c]++;
        }

        return s_count == t_count;
    }
};
