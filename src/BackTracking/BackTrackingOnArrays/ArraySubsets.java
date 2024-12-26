package BackTracking.BackTrackingOnArrays;

import java.util.ArrayList;
import java.util.List;


public class ArraySubsets {

    /**
     * A helper method to recursively find all subsets of the given array.
     *
     * @param nums    The input array of integers.
     * @param list    The list to store all subsets.
     * @param current The current subset being constructed.
     * @param i       The current index in the input array.
     */
    private static void findSubsets(int[] nums, List<List<Integer>> list, ArrayList<Integer> current, int i) {

        // Base case: if the current index is equal to the length of the array, add the current subset to the list
        if (i == nums.length) {
            list.add(new ArrayList<>(current));
            return;
        }

        // Include the current element in the subset and move to the next element
        current.add(nums[i]);
        findSubsets(nums, list, current, i + 1);

        // Exclude the current element from the subset and move to the next element
        current.remove(current.size() - 1);
        findSubsets(nums, list, current, i + 1);
    }

    /**
     * Generates all possible subsets of the given array.
     *
     * @param nums The input array of integers.
     * @return A list of all subsets of the input array.
     */
    public static List<List<Integer>> subsets(int[] nums) {

        List<List<Integer>> list = new ArrayList<>();

        findSubsets(nums, list, new ArrayList<>(), 0);

        return list;
    }
    public static void main(String[] args) {
        int[] nums = {1, 2, 3};

        // Generate all subsets of the array and print the result
        List<List<Integer>> result = subsets(nums);
        System.out.println(result);
    }
}
