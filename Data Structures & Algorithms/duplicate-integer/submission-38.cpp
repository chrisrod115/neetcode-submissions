class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int> dup_num;
        for(int i = 0; i < nums.size(); i++) {
            if (dup_num.find(nums[i]) != dup_num.end()) {
                return true;
            }
            dup_num.insert({nums[i], 0});
        }
        return false;
    }
};