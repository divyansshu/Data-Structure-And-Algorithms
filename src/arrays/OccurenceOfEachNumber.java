package arrays;

import java.util.Arrays;
import java.util.HashMap;
import java.util.TreeMap;

public class OccurenceOfEachNumber {

    // Method to find the occurrences of each number in the array
    public static int[] findOccurences(int[] A) {

        // Create a HashMap to store the occurrences of each number
        HashMap<Integer, Integer> map = new HashMap<>();

        // Iterate through the array
        for(int i = 0; i < A.length; i++) {

            // If the number is already in the map, increment its count
            if(map.containsKey(A[i])) {
                map.put(A[i], map.get(A[i]) + 1);
            }
            // If the number is not in the map, add it with a count of 1
            else {
                map.put(A[i], 1);
            }         
        }

        // Create a TreeMap to sort the numbers by their natural order
        TreeMap<Integer, Integer> treeMap = new TreeMap<>(map);

        // Create an array to store the result
        int[] result = new int[treeMap.size()];

        // Index for the result array
        int i = 0;
        // Iterate through the values in the TreeMap and add them to the result array
        for(int val: treeMap.values()) {
            result[i++] = val;
        }

        // Return the result array
        return result;
    }

    // Main method to test the findOccurences method
    public static void main(String[] args) {

        // Test array
        int[] A = {4, 3, 3};
        // Print the occurrences of each number in the array
        System.out.println(Arrays.toString(findOccurences(A)));
        
    }
    
}
