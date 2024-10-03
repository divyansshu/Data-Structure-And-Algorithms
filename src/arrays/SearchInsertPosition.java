package arrays;

public class SearchInsertPosition {
    public static int searchInsert(int[] nums, int target) {

        int n = nums.length;

        // Case 1: if target is smaller than the first element
        if (target < nums[0])
            return 0;

        // Case 2: if target is greater than the last element
        if (target > nums[n - 1])
            return n;

        // Binary search for the target or the insertion position
        int start = 0;
        int end = n - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        // If the target is not found, start will be the insertion position
        return start;
    }
    public static void main(String[] args) {
        int[] nums = {3,5,7,9,10};
        System.out.println(searchInsert(nums, 8));

    }
}
