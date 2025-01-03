package Algorthims.KadaneAlgorithm;

public class SubArray_Sum {

    public static void main(String[] args) {

        // Initialize the array with given values
        int[] arr = {1, -2, 6, -1, 3};
        
        // Initialize sum to store the current subarray sum
        int sum = 0;
        
        // Initialize max to store the maximum subarray sum found so far
        int max = Integer.MIN_VALUE;

        // Iterate through each element in the array
        for(int i = 0; i < arr.length; i++) {
            // Add the current element to the current subarray sum
            sum += arr[i];
            
            // Update max if the current subarray sum is greater than max
            max = Math.max(sum, max);

            // If the current subarray sum is negative, reset it to 0
            if (sum < 0) {
                sum = 0;
            }
        }

        // Print the maximum sum of any subarray found
        System.out.println("maximum sum of subArray is: "+ max);
    }
}
