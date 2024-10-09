package arrays;

import java.util.HashSet;

public class ContainsDuplicate {
    
    public static boolean containsDuplicate(int[] nums) {

    //     Arrays.sort(nums);
    //     for(int i = 0; i < nums.length; i++) {
    //         if(i+1 < nums.length) {
    //                if(nums[i] == nums[i+1]) {
    //              return true;
    //                } 
    //         }
    //     }
    //     return false;


    HashSet<Integer> set = new HashSet<Integer>();

    for(int i = 0; i < nums.length; i++) {
        if(!set.add(nums[i])) return true;
    }
    return false;
}
    
    public static void main(String[] args) {

        int[] nums = { 1, 2, 3, 1};

        if(containsDuplicate(nums)) 
        System.out.println("yes");
        else System.out.println("No");
        
    }
    
}
