package arrays;

import java.util.HashSet;

public class MissingNumber {

    //method 1: using hash sets
    // time complexity O(n)
    // space complexity O(n)
    public static int missingNumber(int[] nums) {

        HashSet<Integer> set = new HashSet<Integer>();
        int missingNum = 0;

        for (int i = 0; i < nums.length; i++) {
          set.add(nums[i]);
        }

        for(int i = 0; i <= nums.length; i++) {
            if(!set.contains(i)) {
                missingNum = i;
                break;
            }
        }

        return missingNum;
    }

    //method 2: using mathematical formula
    //time complexity O(n)
    //space complexity O(1)
    public static int missingNumber2(int[] nums) {
        int n = nums.length;
        int expectedSum = n * (n+1) / 2;
        int actualSum = 0;

        for(int num: nums) {
            actualSum += num;
        }

        return expectedSum - actualSum;
    }


    // method 3: using nested loops
    // time complexity O(n^2)
    // space complexity O(1)
    public static int missingNumber3(int[] nums) {

        int missingNum = 0;
        
        for(int i = 0; i <= nums.length; i++) {

            int j = 0;

            while(j < nums.length) {
                if(i == nums[j]) break;
            }

            if(j == nums.length) {
                missingNum = i;
                break;
            }
        }

        return missingNum;
    }


    public static void main(String[] args) {
        int[] arr = { 9, 6, 4, 2, 3, 5, 7, 0, 1 };

        System.out.println(missingNumber3(arr));
    }

}
