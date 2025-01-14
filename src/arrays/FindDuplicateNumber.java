package arrays;

import java.util.Arrays;
import java.util.HashSet;

public class FindDuplicateNumber {

    // Method 1: Using a HashSet to find the duplicate number
    //time complexity: O(n)
    //space complexity: O(n)
    public static int findDuplicate1(int[] nums) {
        HashSet<Integer> set = new HashSet<>(); // Create a HashSet to store unique numbers
        int result = 0; // Initialize result to store the duplicate number

        for (int num : nums) { // Iterate through each number in the array
            if (set.contains(num)) // Check if the number is already in the set
                result = num; // If yes, it is the duplicate number
            else
                set.add(num); // If no, add the number to the set
        }
        return result; // Return the duplicate number
    }

    // Method 2: Sorting the array to find the duplicate number
    // time complexity: O(nlogn)
    // space complexity: O(1)
    public static int findDuplicate2(int[] nums) {
        Arrays.sort(nums); // Sort the array

        int i = 0; // Initialize pointer i to the first element
        int j = 1; // Initialize pointer j to the second element

        while (j < nums.length) { // Iterate until j reaches the end of the array
            if (nums[i] == nums[j]) // Check if the current and next elements are the same
                break; // If yes, break the loop as we found the duplicate
            else {
                i++; // Move i to the next element
                j++; // Move j to the next element
            }
        }
        return nums[i]; // Return the duplicate number
    }

    // Method 3: Floyd's Tortoise and Hare (Cycle Detection)
    // time complexity: O(n)
    // space complexity: O(1)
    public static int findDuplicate3(int[] nums) {

        // Initialize two pointers, slow and fast, both starting at the first element
        int slow = nums[0];
        int fast = nums[0];

        // Move slow pointer by one step and fast pointer by two steps until they meet
        do {
            slow = nums[slow]; // Move slow pointer by one step
            fast = nums[nums[fast]]; // Move fast pointer by two steps
        } while (slow != fast); // Continue until they meet

        // Reset slow pointer to the start of the array
        slow = nums[0];
        // Move both pointers by one step until they meet again
        while (slow != fast) {
            slow = nums[slow]; // Move slow pointer by one step
            fast = nums[fast]; // Move fast pointer by one step
        }
        // The meeting point is the duplicate number
        return slow;
    }

    public static void main(String[] args) {
        int[] nums = { 1, 3, 4, 2, 2 }; // Example input array
        System.out.println(findDuplicate1(nums)); // Print the duplicate number
        System.out.println(findDuplicate2(nums)); // Print the duplicate number
        System.out.println(findDuplicate3(nums)); // Print the duplicate number
    }

}
