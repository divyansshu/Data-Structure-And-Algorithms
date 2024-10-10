package arrays;

public class MajorityElement {

    //brute force approach:
    //time complexity: O(n^2)
    public static int majorityElement(int[] nums) {

        int count = 0, max = Integer.MIN_VALUE;
        int element = 0;

        for (int i = 0; i < nums.length; i++) {
            count = 0;
            for (int j = i; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    count++;
                }
            }
            if (count > max) {
                max = count;
                if (max > (nums.length / 2)) {
                    element = nums[i];
                }
            }
        }
        return element;

    }
    public static void main(String[] args) {

        int[] nums = {2,2,1,1,1,2,2};
        System.out.println(majorityElement(nums));
        
    }
    
}
