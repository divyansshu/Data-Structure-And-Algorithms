package arrays.sliding_window;

public class MaxSumSubArray {

    /*
    public static int maxSum(int[] arr, int k) {
    

        // 1: brute force algo

        int maxSum = 0;
        
         * for(int i = 0; i < arr.length; i++) {
         * int j = i;
         * int currSum = 0;
         * for (int p = 0; p < k; p++) {
         * 
         * if(j < arr.length) {
         * currSum += arr[j];
         * j++;
         * }
         * else break;
         * }
         * maxSum = Math.max(maxSum, currSum);
         * currSum = 0;
         * }
         
         * return maxSum;

    }
         */

         //optimized approach
         public static int maxSum(int[] arr, int k) {
            int maxSum = 0;

            for (int i = 0; i < k; i++) {
                maxSum += arr[i]; 
            }
            
           int windowSum = maxSum;
            for(int i = k; i < arr.length; i++) {
                windowSum += arr[i] - arr[i-k];
                maxSum = Math.max(maxSum, windowSum); 
            }

            return maxSum;

         }
    public static void main(String[] args) {
        int[] arr = {1,2,6,2,4,1};
        int k = 3;
        
        System.out.println("Maximum sum of sub array is: "+ maxSum(arr, k));


    }
    
}
