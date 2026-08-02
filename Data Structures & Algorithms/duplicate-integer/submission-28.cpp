class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        int i;
        for (i = 0; i < nums.size(); i++)
        {
            if (seen.find(nums[i]) != seen.end())
            {
                return true;
            }
            seen.insert(nums[i]);
        }
        return false;
    }
};