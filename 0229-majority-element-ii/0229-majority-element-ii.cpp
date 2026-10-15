class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        unordered_map<int, int> mpp;
        vector<int> ls;
        int n = nums.size();
        int mm = (n / 3) + 1;
        for(int i=0; i<n; i++){
            mpp[nums[i]] ++;
            if(mpp[nums[i]] == mm){
                ls.push_back(nums[i]);
            }
        }
        return ls;
    }
};