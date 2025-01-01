package arrays;

import java.util.Arrays;
import java.util.List;

public class SetMatrixZeroes {

    // Function to set matrix zeroes
    public static void setZeroes(List<List<Integer>> matrix) {
        int n = matrix.size(); // Number of rows
        int m = matrix.get(0).size(); // Number of columns

        int[] row = new int[n]; // Array to mark rows that need to be zeroed
        int[] col = new int[m]; // Array to mark columns that need to be zeroed

        // Traverse the matrix to find zeroes
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (matrix.get(i).get(j) == 0) { // If an element is zero
                    row[i] = 1; // Mark the row
                    col[j] = 1; // Mark the column
                }
            }
        }

        // Traverse the matrix again to set zeroes
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (row[i] == 1 || col[j] == 1) { // If the row or column is marked
                    matrix.get(i).set(j, 0); // Set the element to zero
                }
            }
        }
    }

    public static void main(String[] args) {
        // Initialize the matrix
        List<List<Integer>> matrix = Arrays.asList(
            Arrays.asList(0, 1, 2, 0),
            Arrays.asList(3, 4, 5, 2),
            Arrays.asList(1, 3, 1, 5)
        );

        // Call the function to set zeroes
        setZeroes(matrix);
        // Print the modified matrix
        System.out.println(matrix);
    }
}
