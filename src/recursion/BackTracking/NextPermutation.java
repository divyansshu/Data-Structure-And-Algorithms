package BackTracking.BackTrackingOnArrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class NextPermutation {

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
    public static void nextPermutation(int[] arr) {
         List<List<Integer>> result = new ArrayList<>(); // List to store all permutations
        List<Integer> current = new ArrayList<>(); // List to store the current permutation
        boolean[] used = new boolean[arr.length]; // Array to track used elements
        backTrack(arr, used, current, result); // Start backtracking

        System.out.println(result);
        result.sort(Comparator.comparingInt(o -> o.get(0)));
        System.out.println(result);

        List<Integer> nextPermutation = new ArrayList<>();

        for(int i = 0; i < result.size(); i++) {
            List<Integer> innerList = result.get(i);
            int j = 0;
            while(j < innerList.size()) {

                if(arr[j] == innerList.get(j)) j++;
                else break;
            }
            if(j == 3) {
                if(i == result.size() - 1) {
                    nextPermutation = result.get(0);    
                }else {
                   nextPermutation = result.get(i + 1);
                }
            }
        }

        for(int i = 0; i < nextPermutation.size(); i++) {
            arr[i] = nextPermutation.get(i);
        }
                
    }

    public static void main(String[] args) {
        int[] arr = {3,2,1};
        nextPermutation(arr);
        System.out.println(Arrays.toString(arr));

    }
    
}
