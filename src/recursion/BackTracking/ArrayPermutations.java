package BackTracking.BackTrackingOnArrays;

import java.util.ArrayList;
import java.util.List;

public class ArrayPermutations {

    // Helper method to perform backtracking
    private static void backTrack(int[] arr, boolean[] used, List<Integer> current, List<List<Integer>> result) {

        // If the current permutation is complete, add it to the result list
        if(current.size() == arr.length) {
            result.add(new ArrayList<>(current));
            return;
        }

        // Iterate through each element in the array
        for(int i = 0; i < arr.length; i++) {

            // Skip the element if it is already used in the current permutation
            if(used[i])
                continue;

            // Add the element to the current permutation
            current.add(arr[i]);
            // Mark the element as used
            used[i] = true;

            // Recursively call backTrack to continue building the permutation
            backTrack(arr, used, current, result);

            //BackTrack: Remove the last element added to the current permutation
            current.remove(current.size() - 1);
            // Mark the element as unused for the next iteration
            used[i] = false;
        }
    }

    // Method to generate all permutations of the given array
    public static List<List<Integer>> permute(int[] arr) {
        List<List<Integer>> result = new ArrayList<>(); // List to store all permutations
        List<Integer> current = new ArrayList<>(); // List to store the current permutation
        boolean[] used = new boolean[arr.length]; // Array to track used elements
        backTrack(arr, used, current, result); // Start backtracking
        return result; // Return the list of permutations
    }
   
    public static void main(String[] args) {
        int[] arr = { 1,2,3 }; // Input array
        List<List<Integer>> permutations = permute(arr); // Generate permutations
        System.out.println(permutations); // Print the permutations
    }

}
