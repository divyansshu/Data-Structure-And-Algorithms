package arrays;

/*
 * The pivot index is the index where the sum of all the numbers strictly 
 * to the left of the index is equal to the sum of all the numbers strictly to the index's right.
 */

public class Pivot_Index {

    /*
     * Time Complexity: (O(n^2))
     * Space Complexity: (O(1))
     */
    public static int pivotIndex(int[] nums) {
        int leftSum = 0;
        int rightSum = 0;

        // Iterate through each index to find the pivot
        for (int i = 0; i < nums.length; i++) {
            // Calculate the right sum for the current index
            for (int j = i + 1; j < nums.length; j++) {
                rightSum += nums[j];
            }
            // Check if left sum is equal to right sum
            if (leftSum == rightSum)
                return i;
            else {
                // Update the left sum and reset the right sum
                leftSum += nums[i];
                rightSum = 0;
            }
        }
        // If no pivot index is found, return -1
        return -1;
    }

    /*
     * Time Complexity: (O(n))
     * Space Complexity: (O(1))
     */

     public static int pivotIndex_method2(int[] nums) {
        int totalSum = 0;
        int leftSum = 0;

        // Calculate the total sum of the array
        for(int num: nums) {
            totalSum += num;
        }

        // Iterate through the array to find the pivot index
        for(int i = 0; i < nums.length; i++) {
            // Check if left sum is equal to right sum
            if(leftSum == totalSum - leftSum - nums[i]) return i;

            // Update the left sum
            leftSum += nums[i];
        }

        // If no pivot index is found, return -1
        return -1;
     }

    public static void main(String[] args) {
        int[] nums = { 1, 7, 3, 6, 5, 6 };

        System.out.println("pivot index is: " + pivotIndex(nums));
        System.out.println("pivot index is: " + pivotIndex_method2(nums));

    }

}
