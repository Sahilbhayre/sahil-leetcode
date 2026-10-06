class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<vector<int>> ans;
        if (n < 4) return ans;

        sort(nums.begin(), nums.end());

        for (int i = 0; i < n; i++) { // outer loop goes up to n
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            for (int j = i + 1; j < n; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;

                unordered_set<long long> hashSet;

                for (int k = j + 1; k < n; k++) {
                    long long sum = (long long)nums[i] + nums[j] + nums[k];
                    long long fourth = (long long)target - sum;

                    if (hashSet.count(fourth)) {
                        ans.push_back({nums[i], nums[j], (int)fourth, nums[k]});
                        while (k + 1 < n && nums[k] == nums[k + 1]) k++;
                    }
                    hashSet.insert(nums[k]);
                }
            }
        }
        return ans;
    }
};