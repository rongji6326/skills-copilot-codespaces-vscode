import java.util.*;

public class Solution {
    
    public static List<Integer> readRowByRow(int[][] matrix, int n) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                result.add(matrix[i][j]);
            }
        }
        return result;
    }
    
    public static List<Integer> readSpiral(int[][] matrix, int n) {
        List<Integer> result = new ArrayList<>();
        int top = 0, bottom = n - 1, left = 0, right = n - 1;
        
        while (top <= bottom && left <= right) {
            // Read top row
            for (int i = left; i <= right; i++) {
                result.add(matrix[top][i]);
            }
            top++;
            
            // Read right column
            for (int i = top; i <= bottom; i++) {
                result.add(matrix[i][right]);
            }
            right--;
            
            // Read bottom row
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    result.add(matrix[bottom][i]);
                }
                bottom--;
            }
            
            // Read left column
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    result.add(matrix[i][left]);
                }
                left++;
            }
        }
        
        return result;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int x = scanner.nextInt();
        int n = scanner.nextInt();
        
        int[][] matrix = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = scanner.nextInt();
            }
        }
        
        List<Integer> result = new ArrayList<>();
        
        if (x == 0) {
            // For single element
            result.add(matrix[0][0]);
        } else if (x == 45 || x == 47) {
            // Read row by row
            result = readRowByRow(matrix, n);
        } else if (x == 124) {
            // Read in spiral order
            result = readSpiral(matrix, n);
        }
        
        // Output the result
        for (int i = 0; i < result.size(); i++) {
            if (i > 0) System.out.print(" ");
            System.out.print(result.get(i));
        }
        System.out.println();
        
        scanner.close();
    }
}
