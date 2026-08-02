class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> freq_count;
        for(int num: nums) {
            if (freq_count.count(num) > 0) {
                return true;
            }
            freq_count[num]++;
        }
        return false;
    }
};