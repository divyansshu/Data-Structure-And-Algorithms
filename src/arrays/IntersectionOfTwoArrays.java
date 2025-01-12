package arrays;

import java.util.Arrays;
import java.util.HashSet;

public class IntersectionOfTwoArrays {

    // Method to find the intersection of two arrays
    public static int[] intersection(int[] nums1, int[] nums2) {

        // Create a HashSet to store unique elements from the first array
        HashSet<Integer> set = new HashSet<>();

        // Add each element of the first array to the set
        for(int num: nums1) {
            set.add(num);
        }

        // Create another HashSet to store the intersection result
        HashSet<Integer> resultSet = new HashSet<>();
        
        // Check each element of the second array
        for(int num: nums2) {
            // If the element is present in the first set, add it to the result set
            if(set.contains(num)) resultSet.add(num); 
        }

        // Convert the result set to an array
        int[] resultArray = new int[resultSet.size()];
        int k = 0;
        // Copy each element from the result set to the result array
        for(int element: resultSet) {
            resultArray[k++] = element;
        }
        // Return the result array
        return resultArray;
    }

    // Main method to test the intersection method
    public static void main(String[] args) {

        // Define two arrays
        int[] nums1 = {1,2,2,1};
        int[] nums2 = {2,2};

        // Print the intersection of the two arrays
        System.out.println(Arrays.toString(intersection(nums1, nums2)));
        
    }
    
}
