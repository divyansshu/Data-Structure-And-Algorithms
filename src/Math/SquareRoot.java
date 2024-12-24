public class SquareRoot {

    // Method to calculate the integer part of the square root of a given number x
    public static int mySqrt(int x) {
        // If x is 0 or 1, return x as the square root of 0 is 0 and the square root of 1 is 1
        if (x <= 1)
            return x;

        // Initialize the left and right pointers for binary search
        int left = 1;
        int right = x;
        int result = 0;

        // Perform binary search to find the square root
        while (left <= right) {
            // Calculate the mid value
            int mid = (left + right) / 2;

            // Check if mid is less than or equal to x divided by mid
            if (mid <= x / mid) {
                // If true, mid is a potential result, store it
                result = mid;
                // Move the left pointer to mid + 1 to search in the right half
                left = mid + 1;
            } else {
                // If false, move the right pointer to mid - 1 to search in the left half
                right = mid - 1;
            }
        }
        // Return the result which is the integer part of the square root
        return result;
    }

    // Main method to test the mySqrt method
    public static void main(String[] args) {
        // Print the square root of 25
        System.out.println(mySqrt(25));
        // Print the square root of 27
        System.out.println(mySqrt(27));
    }
    
}
