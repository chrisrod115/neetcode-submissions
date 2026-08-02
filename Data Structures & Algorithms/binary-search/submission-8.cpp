class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size();
        while (l < r) {
            int middle = l + (r - l)/2;
            if (nums[middle] > target) {
                r = middle;
            }
            else {
                l = middle + 1;
            }
        }
        return (l > 0 && nums[l - 1] == target) ? l - 1: -1;
    }
};
