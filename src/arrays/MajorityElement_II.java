package arrays;

import java.util.ArrayList;
import java.util.List;

public class MajorityElement_II {

    // Function to find a majority element that appears more than n/3 times
    //time complexity: O(n)
    //space complexity: O(1)
    public static int repeatedNumber(final List<Integer> nums) {
        int candidate1 = -1; // First candidate for majority element
        int candidate2 = -1; // Second candidate for majority element
        int count1 = 0; // Count for first candidate
        int count2 = 0; // Count for second candidate
        int n = nums.size(); // Size of the input list

        // First pass to find potential candidates
        for (int num : nums) {
            if (num == candidate1) {
                count1++; // Increment count1 if num matches candidate1
            } else if (num == candidate2) {
                count2++; // Increment count2 if num matches candidate2
            } else if (count1 == 0) {
                candidate1 = num; // Update candidate1 if count1 is zero
                count1 = 1;
            } else if (count2 == 0) {
                candidate2 = num; // Update candidate2 if count2 is zero
                count2 = 1;
            } else {
                count1--; // Decrement both counts if num matches neither candidate
                count2--;
            }
        }

        // Reset counts for validation
        count1 = 0;
        count2 = 0;

        // Second pass to validate the candidates
        for (int num : nums) {
            if (num == candidate1) count1++; // Count occurrences of candidate1
            else if (num == candidate2) count2++; // Count occurrences of candidate2
        }

        // Check if any candidate occurs more than n/3 times
        if (count1 > n / 3) return candidate1;
        if (count2 > n / 3) return candidate2;

        return -1; // Return -1 if no majority element found
    }

    // Function to find all majority elements that appear more than n/3 times
    // time complexity: O(n)
    // space complexity: O(n)
    public static List<Integer> repeatedNumberList(final List<Integer> nums) {
        List<Integer> result = new ArrayList<>(); // List to store result
        int candidate1 = -1; // First candidate for majority element
        int candidate2 = -1; // Second candidate for majority element
        int count1 = 0; // Count for first candidate
        int count2 = 0; // Count for second candidate
        int n = nums.size(); // Size of the input list

        // First pass to find potential candidates
        for (int num : nums) {
            if (num == candidate1) {
                count1++; // Increment count1 if num matches candidate1
            } else if (num == candidate2) {
                count2++; // Increment count2 if num matches candidate2
            } else if (count1 == 0) {
                candidate1 = num; // Update candidate1 if count1 is zero
                count1 = 1;
            } else if (count2 == 0) {
                candidate2 = num; // Update candidate2 if count2 is zero
                count2 = 1;
            } else {
                count1--; // Decrement both counts if num matches neither candidate
                count2--;
            }
        }

        // Reset counts for validation
        count1 = 0;
        count2 = 0;

        // Second pass to validate the candidates
        for (int num : nums) {
            if (num == candidate1) count1++; // Count occurrences of candidate1
            else if (num == candidate2) count2++; // Count occurrences of candidate2
        }

        // Add candidates to result if they occur more than n/3 times
        if (count1 > n / 3) result.add(candidate1);
        if (count2 > n / 3) result.add(candidate2);

        return result; // Return the list of majority elements
    }

    public static void main(String[] args) {
        List<Integer> nums = new ArrayList<>();
        nums.add(1);
        nums.add(2);
        // nums.add(2);

        System.out.println(repeatedNumber(nums)); // Test repeatedNumber function
        System.out.println(repeatedNumberList(nums)); // Test repeatedNumberList function
    }
}
