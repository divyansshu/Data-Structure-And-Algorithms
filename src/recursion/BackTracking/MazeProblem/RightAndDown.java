package BackTracking.MazeProblem; // Define the package name

public class RightAndDown { // Define the class RightAndDown

    // Method to calculate the number of paths from the top-left to the bottom-right of a grid
    public static int numberOfPaths(int row, int col) {
        
        // Base case: If either row or column is 1, there is only one path (straight line)
        if (row == 1 || col == 1) {
            return 1;
        }

        // Recursive case: Sum of paths from the cell to the left and the cell above
        return numberOfPaths(row, col - 1) + numberOfPaths(row - 1, col);
    }

    public static void main(String[] args) {
        // Define a 3x3 maze (not used in the current logic)
        int[][] maze = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

        // Print the number of paths in a 3x3 grid
        System.out.println(numberOfPaths(3, 3));
    }
}
