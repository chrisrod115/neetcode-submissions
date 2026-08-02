class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> num_set(nums.begin(), nums.end());
        int res = 0; 

        for (int n: num_set)
        {
            if (num_set.find(n - 1) == num_set.end())
            {
                int longest = 1;
                while (num_set.find(n+1) != num_set.end())
                {
                    longest++;
                    n++;
                }
                res = max(res, longest);
            }
        }
        return res;
    }
};
