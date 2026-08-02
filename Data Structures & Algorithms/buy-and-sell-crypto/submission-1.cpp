class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int best = 0;
        int l = 0, r = 1;
        while (r < prices.size()) {
            if (prices[l] < prices[r]) {
                int profit = prices[r] - prices[l];
                best = max(best, profit);
            }
            else {
                l = r;
            }
            r++;
        }
        return best;
    }
};
