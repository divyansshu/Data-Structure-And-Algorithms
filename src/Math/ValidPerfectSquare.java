package Math;

public class ValidPerfectSquare {

    // Method to check if a number is a perfect square
    public static boolean perfectSquare(int n) {
        int left = 1;
        int right = n;

        // Binary search to find the perfect square
        while(left <= right) {
            int mid = (left + right) / 2;
            
            //The result is cast to a long to handle large numbers and avoid overflow.
            long midSquare = (long) mid * mid;

            // Check if midSquare is equal to n
            if(midSquare == n) return true;
            // If midSquare is less than n, search in the right half
            else if(midSquare < n) left = mid + 1;
            // If midSquare is greater than n, search in the left half
            else right = mid - 1;
        }
        // Return false if no perfect square is found
        return false;
    }

    // Main method to test the perfectSquare method
    public static void main(String[] args) {
        int n = 31;
        System.out.println(perfectSquare(n)); // Output: false
    }
    
}
