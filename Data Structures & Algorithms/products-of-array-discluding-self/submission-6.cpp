class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        /*
        [1,2,3]
        res = [6, 3, 2]
        
        [0, 1, 2] ==> nums.size() = 3
        res [1,1,1]
        nums[1,2,3]
        pre = [1, 1, 2]
        1. build the res array with and array of 1's
        2. find the product of the array up to the number (for loop)
        3. multiply that number by the previous which is the res[pre]
        4. update the index at that number.
        5. not for the post --> set it to 1
        6. from the ending multiple everything after that index 
        7. update the res array
        */
        int n = nums.size();
        vector<int> res(n, 1);
        for(int i = 1; i < n; i++)
        {
            res[i] = res[i - 1] * nums[i - 1];
        }
        int post = 1;
        for (int i = n - 1; i >= 0; i--)
        {
            res[i] *= post;
            post *= nums[i];
        }
        return res;
    }
};
