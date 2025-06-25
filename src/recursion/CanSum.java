package recursion;

public class CanSum {
    public static boolean canSum(int[] arr, int target) {
        // for(int i = 0; i < arr.length; i++) {
        //     if(target % arr[i] == 0) {
        //         return true;
        //     }
        // }
        // return false;

        if(target == 0) return true;
        if(target < 0) return false;

        for(int i = 0; i < arr.length; i++) {
            int rem = target - arr[i];
            return canSum(arr, rem);
        }
        return false;
    }
    public static void main(String[] args) {
        int[] nums = {2,4,6};
        System.out.println(canSum(nums, 99));
    }
    
}
