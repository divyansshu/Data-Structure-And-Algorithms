package arrays;

public class PickFromBothSides {


    // This method calculates the maximum sum of B elements picked from either end of the array.
    public static int solve(int[] A, int B) {
        // Get the length of the array
        int N = A.length;
        
        // Initialize the current sum with the sum of the first B elements
        int currentSum = 0;
        for (int i = 0; i < B; i++) {
            currentSum += A[i];
        }

        // Initialize the maximum sum with the current sum
        int maxSum = currentSum;

        // Iterate through the array to find the maximum sum by picking elements from both ends
        for (int i = 0; i < B; i++) {
            // Update the current sum by subtracting the element from the start and adding the element from the end
            currentSum = currentSum - A[B - i - 1] + A[N - i - 1];
            // Update the maximum sum if the current sum is greater
            maxSum = Math.max(currentSum, maxSum);
        }
        return maxSum;
    }

    public static void main(String[] args) {
        // Example usage of the solve method
        int[] A = { -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35 };
        int B = 48;
        System.out.println(A.length);
        System.out.println(solve(A,B));
    }
    
}
