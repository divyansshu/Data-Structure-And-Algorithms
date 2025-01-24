package arrays;

public class UnsortedContinuousSubArray {

    public static int findUnsortedSubArray(int[] nums) {
        int n = nums.length;
        int left = 0, right = n - 1;

        // Find the first element from the left that is out of order
        while (left < n - 1 && nums[left] <= nums[left + 1]) {
            left++;
        }

        // If the array is already sorted, return 0
        if (left == n - 1)
            return 0;

        // Find the first element from the right that is out of order
        while (right >= 0 && nums[right] >= nums[right - 1]) {
            right--;
        }

        // Find the minimum and maximum values in the unsorted subarray
        int subArrayMin = Integer.MAX_VALUE, subArrayMax = Integer.MIN_VALUE;
        for (int i = left; i <= right; i++) {
            subArrayMin = Math.min(subArrayMin, nums[i]);
            subArrayMax = Math.max(subArrayMax, nums[i]);
        }

        // Extend the left boundary if needed
        while (left > 0 && subArrayMin < nums[left - 1])
            left--;
        // Extend the right boundary if needed
        while (right < n - 1 && subArrayMax > nums[right + 1])
            right++;

        // Return the length of the unsorted subarray
        return right - left + 1;
    }

    public static void main(String[] args) {
        int[] nums = {2,6,4,8,10,9,15};
        System.out.print("length of unsorted sub array: ");
        System.out.println(findUnsortedSubArray(nums));
    }
    
}
