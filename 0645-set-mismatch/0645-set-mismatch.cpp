class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
            int n = nums.size();
            int repeating = -1;
            int missing = -1;
            for(int i = 1; i <= n; i++){
                int cnt = 0;
                for(int j = 0; j < n; j++){
                    if(nums[j] == i){
                        cnt++;
                    }
                }
                if(cnt == 2) repeating = i;
                else if(cnt == 0) missing = i;
                if(repeating != -1 && missing != -1){
                    break;
                }
            }
            return {repeating, missing};
    }
};