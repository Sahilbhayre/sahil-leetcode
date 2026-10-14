class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> result;
        
        for (int n = 0; n < numRows; n++) {
            vector<int> currentRow;
            long long val = 1; // nC0 is always 1
            
            for (int r = 0; r <= n; r++) {
                currentRow.push_back(val);
                val = val * (n - r);
                val = val / (r + 1);
            }
            result.push_back(currentRow);
        }
        
        return result;
    }
};