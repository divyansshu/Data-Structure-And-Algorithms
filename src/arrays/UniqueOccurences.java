package arrays;

import java.util.HashMap;
import java.util.HashSet;

public class UniqueOccurences {

    // Method to check if all occurrences of elements in the array are unique
    public static boolean uniqueOccurences(int[] arr) {
        // Create a HashMap to store the frequency of each element
        HashMap<Integer, Integer> map = new HashMap<>();

        // Iterate through the array to populate the frequency map
        for(int i = 0; i < arr.length; i++) {
            // If the element is already in the map, increment its count
            if(map.containsKey(arr[i])) {
                map.put(arr[i], map.get(arr[i])+1);
            } else {
                // Otherwise, add the element to the map with a count of 1
                map.put(arr[i], 1);
            }
        }

        // Create a HashSet to store the frequencies
        HashSet<Integer> set = new HashSet<>();

        // Iterate through the values (frequencies) in the map
        for(int val: map.values()) {
            // If the frequency is already in the set, return false (not unique)
            if(set.contains(val)) return false;
            else set.add(val); // Otherwise, add the frequency to the set
        }
        // If all frequencies are unique, return true
        return true;
    }

    public static void main(String[] args) {
        // Test the uniqueOccurences method with a sample array
        int[] arr = {1, 2};

        // Print the result of the method
        System.out.println(uniqueOccurences(arr));
    }
    
}
