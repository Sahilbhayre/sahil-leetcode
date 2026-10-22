class Solution {
private:
    void merge(vector<pair<int, int>>& arr, int left, int mid, int right, vector<int>& ans) {
        int i = left;
        int j = mid + 1;  
        int rightCount = 0;
        
        vector<pair<int, int>> temp;
        
        while (i <= mid && j <= right) {
            if (arr[i].first <= arr[j].first) {
                ans[arr[i].second] += rightCount;
                temp.push_back(arr[i++]);
            } 
            else {
                rightCount++;
                temp.push_back(arr[j++]);
            }
        }
        
        while (i <= mid) {
            ans[arr[i].second] += rightCount;
            temp.push_back(arr[i++]);
        }
        
        while (j <= right) {
            temp.push_back(arr[j++]);
        }
        
        for (int k = left; k <= right; k++) {
            arr[k] = temp[k - left];
        }
    }

    void mergeSort(vector<pair<int, int>>& arr, int left, int right, vector<int>& ans) {
        if (left >= right) return;
        
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid, ans);
        mergeSort(arr, mid + 1, right, ans);
        merge(arr, left, mid, right, ans);
    }

public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n, 0);
        vector<pair<int, int>> arr(n);
  
        for (int i = 0; i < n; i++) {
            arr[i] = {nums[i], i};
        }
        
        mergeSort(arr, 0, n - 1, ans);
        return ans;
    }
};