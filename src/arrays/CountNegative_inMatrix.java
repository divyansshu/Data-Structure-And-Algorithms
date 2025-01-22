package arrays;

public class CountNegative_inMatrix {

    /*
     * time complexity: O(m x log(n))
     * space complexity: O(1)
     */
    public static int countNegatives(int[][] matrix) {
        int count = 0; 
        int row = matrix.length; 
        int col = matrix[0].length; 

        for(int i = 0; i < row; i++) { // Iterate through each row
            int low = 0; // Initialize the low pointer for binary search
            int high = col - 1; // Initialize the high pointer for binary search
            while(low <= high) { // Perform binary search in the current row
                int mid = (low + high) / 2; // Calculate the mid index

                if(matrix[i][mid] < 0) { // If the mid element is negative
                    high = mid - 1; // Move the high pointer to the left
                } else { // If the mid element is non-negative
                    low = mid + 1; // Move the low pointer to the right
                }
            }
            count += (col - low); // Add the count of negative numbers in the current row
        }
        return count; // Return the total count of negative numbers
    }

    /*
     * time complexity: O(m + n)
     * space complexity: O(1)
     */
    public static int countNegatives_method2(int[][] matrix) {
        int rowSize = matrix.length; 
        int colSize = matrix[0].length; 
        int count = 0; 

        int rowNum = 0; // Initialize the row pointer
        int colNum = colSize - 1; // Initialize the column pointer

        while(rowNum < rowSize && colNum >= 0) { // Traverse the matrix from top-right to bottom-left
            if(matrix[rowNum][colNum] < 0) { // If the current element is negative
               count += (rowSize - rowNum); // Add the count of negative numbers in the current column
               colNum--; // Move the column pointer to the left
            } else { // If the current element is non-negative
                rowNum++; // Move the row pointer down
            }
        }
        return count; // Return the total count of negative numbers
    }

    public static void main(String[] args) {
        int[][] matrix = {{4, 3, 2, -1}, {3, 2, 1, -1}, {1, 1, -1, -2}, {-1, -1, -2, -3}}; 
        System.out.println(countNegatives(matrix)); 
        System.out.println(countNegatives_method2(matrix)); 
    }
    
}
