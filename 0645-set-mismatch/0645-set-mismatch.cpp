class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        int repeating = -1;
        int missing = -1;

        // 1. Brute Force
        // for(int i = 1; i <= n; i++){
        //     int cnt = 0;
        //     for(int j = 0; j < n; j++){
        //         if(nums[j] == i){
        //             cnt++;
        //         }
        //     }
        //     if(cnt == 2) repeating = i;
        //     else if(cnt == 0) missing = i;
        //     if(repeating != -1 && missing != -1){
        //         break;
        //     }
        // }


        // 2. Better Solution
        // vector<int> hash(n + 1, 0);
        // for(int i = 0; i < n; i++){
        //     hash[nums[i]]++;
        // }

        // for(int i = 1; i <= n; i++){
        //     if(hash[i] == 2) repeating = i;
        //     else if(hash[i] == 0) missing = i;

        //     if(repeating != -1 && missing != -1){
        //         break;
        //     }
        // }
        // return {repeating, missing};


        // 3. Optimal Solution using Mathemeatics
        long long SN = ((long long)n * (n+1)) / 2;
        long long S2N = ((long long)n * (n+1) * (2*n+1)) / 6;
        long long S = 0, S2 = 0;
        for(int i = 0; i < n; i++){
            S += nums[i];
            S2 += (long long)nums[i] * (long long)nums[i];
        }
        long long val1 = S - SN;
        long long val2 = S2 - S2N;
        val2 = val2 / val1;
        long long x = (val1 + val2) / 2;
        long long y = x - val1;

        return {(int)x, (int)y};
    }
};