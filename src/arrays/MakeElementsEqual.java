package arrays;

import java.util.HashSet;
import java.util.Set;

public class MakeElementsEqual {

    // Helper method to find the intersection of two sets
    private static Set<Integer> findIntersection(Set<Integer> possibleValues, Set<Integer> set) {
        Set<Integer> result = new HashSet<>();
        // Iterate through possibleValues and add common elements to result
        for(int val: possibleValues) {
            if(set.contains(val)) {
                result.add(val);
            }
        }
        return result;
    }

    // Method to check if all elements in the array can be made equal by adding or subtracting x
    public static boolean makeEqual(int[] arr, int x) {
        // If the array has only one element, return true
        if(arr.length == 1) return true;

        // Initialize possibleValues with the possible values for the first element
        Set<Integer> possibleValues = new HashSet<>();
        possibleValues.add(arr[0] + x);
        possibleValues.add(arr[0] - x);
        possibleValues.add(arr[0]);

        // Iterate through the rest of the array
        for(int i = 1; i < arr.length; i++) {
            Set<Integer> currentValues = new HashSet<>();
            // Add possible values for the current element
            currentValues.add(arr[i] + x);
            currentValues.add(arr[i] - x);
            currentValues.add(arr[i]);

            // Find the intersection of possibleValues and currentValues
            possibleValues = findIntersection(possibleValues, currentValues);
            // If there are no common values, return false
            if (possibleValues.isEmpty())
                return false;
        }

        // If there are common values for all elements, return true
        return true;
    }

    public static void main(String[] args) {
        int[] arr = {2, 3, 1};
        // Test the makeEqual method with the given array and x value
        System.out.println(makeEqual(arr, 1));
    }
    
}
