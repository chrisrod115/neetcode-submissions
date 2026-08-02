class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map <char, int> s_count;
        unordered_map <char, int> t_count;
        int s_length = s.length();

        if (s.length() != t.length())
        {
            return false;
        }

        for (int i = 0; i < s_length; i++)
        {
            s_count[s[i]]++;
            t_count[t[i]]++;
        }
        return s_count == t_count;
    }
};
