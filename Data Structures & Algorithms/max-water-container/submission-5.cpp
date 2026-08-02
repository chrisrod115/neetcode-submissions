class Solution {
public:
    int maxArea(vector<int>& heights) {
        /*
        [1,7,2,5,4,7,3,6]
           l     r
        This is actually height * width
        */
        int l = 0, r = heights.size() - 1;
        int res = 0;
        while (l < r)
        {
            int smallest = min(heights[l], heights[r]);
            int volume = smallest * (r - l);

            if (heights[l] >= heights[r])
            {
                r--;
            }
            
            else
            {
                l++;
            }

            res = max(res, volume);
        }
        return res;
    }
};
