class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int arr[n][n];
        // 1. Brute Force
        // for(int i=0; i<n; i++){
        //     for(int j=0; j<n; j++){
        //         arr[j][n-i-1] = matrix[i][j];
        //     }
        // }
        // for(int i=0; i<n; i++){
        //     for(int j=0; j<n; j++){
        //         matrix[i][j] = arr[i][j];
        //     }
        // }

        // 2. Optimal Sol
        for(int i=0; i<n-1; i++){
            for(int j=i+1; j<n; j++){
                swap(matrix[i][j], matrix[j][i]);
            }
        }
        for(int i=0; i<n; i++){
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }

};