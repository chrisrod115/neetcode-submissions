class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<vector<int>> buckets(nums.size() + 1);
        unordered_map<int, int> count;

        for (int i = 0; i < nums.size(); i++)
        {
            count[nums[i]]++;
        }

        for (const auto& entry: count)
        {
            buckets[entry.second].push_back(entry.first);
        }

        vector<int> res;
        for (int j = buckets.size() - 1; j > 0; j --)
        {
            for (int n: buckets[j])
            {
                res.push_back(n);
                if (res.size() == k)
                {
                    return res;
                }
            }
        }
        return res;

    }
};
