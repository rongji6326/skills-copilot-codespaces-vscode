#include <iostream>
#include <vector>
using namespace std;

vector<int> readRowByRow(vector<vector<int>>& matrix, int n) {
    vector<int> result;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            result.push_back(matrix[i][j]);
        }
    }
    return result;
}

vector<int> readSpiral(vector<vector<int>>& matrix, int n) {
    vector<int> result;
    int top = 0, bottom = n - 1, left = 0, right = n - 1;
    
    while (top <= bottom && left <= right) {
        // Read top row
        for (int i = left; i <= right; i++) {
            result.push_back(matrix[top][i]);
        }
        top++;
        
        // Read right column
        for (int i = top; i <= bottom; i++) {
            result.push_back(matrix[i][right]);
        }
        right--;
        
        // Read bottom row
        if (top <= bottom) {
            for (int i = right; i >= left; i--) {
                result.push_back(matrix[bottom][i]);
            }
            bottom--;
        }
        
        // Read left column
        if (left <= right) {
            for (int i = bottom; i >= top; i--) {
                result.push_back(matrix[i][left]);
            }
            left++;
        }
    }
    
    return result;
}

int main() {
    int x, n;
    cin >> x >> n;
    
    vector<vector<int>> matrix(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }
    
    vector<int> result;
    
    if (x == 0) {
        // For single element
        result.push_back(matrix[0][0]);
    } else if (x == 45 || x == 47) {
        // Read row by row
        result = readRowByRow(matrix, n);
    } else if (x == 124) {
        // Read in spiral order
        result = readSpiral(matrix, n);
    }
    
    // Output the result
    for (int i = 0; i < result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    
    return 0;
}
