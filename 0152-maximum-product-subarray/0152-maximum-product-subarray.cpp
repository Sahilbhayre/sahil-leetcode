class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        int maxi = INT_MIN;

        // 1. Brute Force
        // for(int i = 0; i < n; i++){
        //     for(int j = i; j < n; j++){
        //         int prod = 1;
        //         for(int k = i; k <= j; k++){
        //             prod = prod * nums[k];
        //         }
        //         maxi = max(maxi, prod);
        //     }
        // }

        // 2. Better Approach
        for(int i = 0; i < n; i++){
            int prod = 1;
            for(int j = i; j < n; j++){
                prod = prod * nums[j];
                maxi = max(maxi, prod);
            }
        }
        return maxi;
    }
};