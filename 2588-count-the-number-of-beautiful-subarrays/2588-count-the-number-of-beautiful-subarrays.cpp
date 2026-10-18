class Solution {
public:
    long long beautifulSubarrays(vector<int>& nums) {
        int n = nums.size();
        unordered_map<long long, long long>prefixCnt;
        long long xorr = 0;
        long long cnt = 0;

        prefixCnt[0] = 1;
        for(int num : nums){
            xorr = xorr ^ num;
            if(prefixCnt.find(xorr) != prefixCnt.end()){
                cnt += prefixCnt[xorr];
            }
            prefixCnt[xorr]++;
        }
        return cnt;
    }
};