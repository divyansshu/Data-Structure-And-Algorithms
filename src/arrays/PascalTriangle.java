package arrays;

import java.util.Arrays;

public class PascalTriangle {

    // Method to generate Pascal's Triangle with a given number of rows
    public static int[][] generate(int numRows) {
        // Initialize a 2D array to hold the values of Pascal's Triangle
        int[][] triangle = new int[numRows][];

        // Loop through each row
        for(int row = 0; row < numRows; row++) {
            // Initialize the current row with the appropriate number of columns
            triangle[row] = new int[row + 1];
            // Loop through each column in the current row
            for(int col = 0; col <= row; col++) {
                // The first and last elements in each row are always 1
                if(col == 0 || col == row) {
                    triangle[row][col] = 1;
                } else {
                    // Each element is the sum of the two elements directly above it
                    triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col];
                }
            }
        }
        // Return the generated Pascal's Triangle
        return triangle;
    }

    public static void main(String[] args) {
        int n = 5; // Number of rows for Pascal's Triangle
        int[][] triangle = generate(n); // Generate the triangle

        // Print each row of the triangle
        for(int[] row : triangle) {
            System.out.println(Arrays.toString(row));
        }
    }
}
