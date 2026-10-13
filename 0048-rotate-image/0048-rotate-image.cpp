class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int arr[n][n];
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                arr[j][n-i-1] = matrix[i][j];
            }
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                matrix[i][j] = arr[i][j];
            }
        }
    }
};