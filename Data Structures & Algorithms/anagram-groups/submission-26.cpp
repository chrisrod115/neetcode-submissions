class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> res;
        for (auto s: strs) {
            vector<int> counter(26, 0);
            for (auto c: s) {
                counter[c - 'a']++;
            }
            string key = to_string(counter[0]);
            for (int i = 1; i < 26; i++) {
                key += ',' + to_string(counter[i]);
            }
            res[key].push_back(s);
        }
        vector<vector<string>> result;
        for (const auto& pair: res) {
            result.push_back(pair.second);
        }
        return result;
    }
};
