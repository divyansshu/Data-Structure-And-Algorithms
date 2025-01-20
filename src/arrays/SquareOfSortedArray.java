package arrays;

import java.util.Arrays;

public class SquareOfSortedArray {

    // Method to square each element in the array and return a sorted array of the squares
    public static int[] squareAndSort(int[] nums) {
        int i = 0; // Initialize left pointer
        int j = nums.length - 1; // Initialize right pointer
        int k = nums.length - 1; // Initialize position for the result array from the end
        int[] result = new int[nums.length]; // Create a result array to store the squares

        // Loop until the left pointer is less than or equal to the right pointer
        while (i <= j) {
            int leftSq = nums[i] * nums[i]; // Square the element at the left pointer
            int rightSq = nums[j] * nums[j]; // Square the element at the right pointer

            // Compare the squares and place the larger one at the current position in the result array
            if (leftSq > rightSq) {
                result[k--] = leftSq; // Place the left square in the result array and move left pointer
                i++;
            } else {
                result[k--] = rightSq; // Place the right square in the result array and move right pointer
                j--;
            }
        }
        return result; // Return the sorted array of squares
    }

    public static void main(String[] args) {
        int[] nums = { -4, -1, 0, 3, 10 }; // Input array
        System.out.println(Arrays.toString(squareAndSort(nums))); // Print the sorted array of squares
    }

}
