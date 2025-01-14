package arrays;

import java.util.HashMap;

// The majority element is the element that appears more than ⌊n / 2⌋ times. 
public class MajorityElement {

    // Brute force approach:
    // Time complexity: O(n^2)
    public static int majorityElement(int[] nums) {
        int max = Integer.MIN_VALUE; // Initialize count and max variables
        int element = 0; // Variable to store the majority element

        // Iterate through each element in the array
        for (int i = 0; i < nums.length; i++) {
            int count = 0; // Reset count for each element
            // Count occurrences of the current element
            for (int j = i; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    count++;
                }
            }
            // Update max and element if the current element count is greater than max
            if (count > max) {
                max = count;
                // Check if the current element is the majority element
                if (max > (nums.length / 2)) {
                    element = nums[i];
                }
            }
        }
        return element; // Return the majority element
    }

    // Optimized approach
    // time complexity: O(n)
    // space complexity: O(n)
    public static int majorityElement2(int[] nums) {
        HashMap<Integer, Integer> countMap = new HashMap<>(); // HashMap to store element counts
        int majorityCount = nums.length / 2; // Calculate the majority count threshold

        // Count the occurrences of each element
        for (int num : nums) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1); // Update the count of the current element
            // Check if the current element is the majority element
            if (countMap.get(num) > majorityCount) {
                return num; // Return the majority element
            }
        }

        // If no majority element is found (should not happen as per problem constraints)
        throw new IllegalArgumentException("No majority element found");
    }

    public static void main(String[] args) {
        int[] nums = {2, 2, 1, 1, 1, 2, 2}; // Example array
        System.out.println(majorityElement(nums)); // Print the result of the brute force approach
        System.out.println(majorityElement2(nums)); // Print the result of the optimized approach
    }
}
