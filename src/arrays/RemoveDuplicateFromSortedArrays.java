package arrays;

public class RemoveDuplicateFromSortedArrays {
    public static int removeDuplicates(int[] nums) {
        int j = 1;
        int k = 1;
        for(int i = 0; i < nums.length; i++) {
            if (j < nums.length) {
                if(nums[i] == nums[j]) {
                    j++;
                }
                else {
                    nums[k] = nums[j];
                    j++;
                    k++;
                }
            }
        }
        return k;
    }
    public static void main(String[] args) {
        int[] arr = {0,0,1,1,1,2,2,3,3,4};
        int k = removeDuplicates(arr);

        for(int i = 0; i < k; i++) {
            System.out.print(arr[i]+" ");
        }


    }
}
