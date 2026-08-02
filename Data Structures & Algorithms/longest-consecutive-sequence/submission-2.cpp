class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        /*
        Input: nums = [2,20,4,10,3,4,5]
        figure out if the item is a head or not
        */
        int res = 0;
        unordered_set<int> nums_set(nums.begin(), nums.end());

        for (auto n: nums_set)
        {
            if (nums_set.find(n-1) == nums_set.end())
            {
                int length = 1;
                while (nums_set.find(n+1) != nums_set.end())
                {
                    length++;
                    n++;
                }
                res = max(length, res);
            }
        } 
        return res;

    }
};
