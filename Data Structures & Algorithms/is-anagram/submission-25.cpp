class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length())
        {
            return false;
        }

        unordered_map<char, int> s_size;
        unordered_map<char, int> t_size;

        for(int i = 0; i < s.length(); i++)
        {
            s_size[s[i]]++;
            t_size[t[i]]++;
        }

        return s_size == t_size;
    }
};
