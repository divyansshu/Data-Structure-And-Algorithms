package arrays;

// rotate matrix by 90 degree clockwise
public class RotateMatrix {

    public static void rotate(int[][] matrix) {

        int left = 0; // Initialize the left pointer to the first column
        int right = matrix.length - 1; // Initialize the right pointer to the last column

        while(left < right) { // Continue until the left pointer crosses the right pointer
            int top = left; // Initialize the top pointer to the current left pointer
            int bottom = right; // Initialize the bottom pointer to the current right pointer

            for(int i = 0; i < right - left; i++) { // Loop through the elements in the current layer

                int topleft = matrix[top][left + i]; // Store the top-left element

                matrix[top][left + i] = matrix[bottom - i][left]; // Move bottom-left to top-left

                matrix[bottom - i][left] = matrix[bottom][right - i]; // Move bottom-right to bottom-left

                matrix[bottom][right - i] = matrix[top + i][right]; // Move top-right to bottom-right

                matrix[top + i][right] = topleft; // Move top-left to top-right

            }
            left++; // Move the left pointer inward
            right--; // Move the right pointer inward
        }
    }

    public static void main(String[] args) {
        int[][] matrix = {{1,2,3}, {4,5,6}, {7,8,9}}; // Initialize a 3x3 matrix

        System.out.println("Matrix before rotation");
        for(int i = 0; i < matrix.length; i++) { // Loop through rows
            for(int j = 0; j < matrix.length; j++) { // Loop through columns
                System.out.print(matrix[i][j] + " "); // Print each element
            }
            System.out.println(); // New line after each row
        }
        
        System.out.println("Matrix after rotation");
        rotate(matrix); // Rotate the matrix by 90 degrees clockwise
        for (int i = 0; i < matrix.length; i++) { // Loop through rows
            for (int j = 0; j < matrix.length; j++) { // Loop through columns
                System.out.print(matrix[i][j] + " "); // Print each element
            }
            System.out.println(); // New line after each row
        }

    }
    
}
