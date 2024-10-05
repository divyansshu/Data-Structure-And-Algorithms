package arrays.sliding_window;

public class MaxSubArray {
    public static void main(String[] args) {

        int[] arr = {1, -2, 6, -1, 3};
        int sum = 0;
        int max = Integer.MIN_VALUE;

        /** Brute force */
        /*
        for(int i = 0; i < arr.length; i++) {
            for(int j = i+1; j < arr.length; j++) {
                sum = 0;
                for(int k = i; k <= j; k++) {
                    System.out.print(arr[k]+", ");
                     sum += arr[k];
                }
                System.out.println("\n sum of sub array :"+ sum);
                if(sum > max) {
                    max = sum;
                }
            }
        }
        System.out.println("maximum sum of sub array is : "+ max);
        */

        /** prefix sum Array */

        int[] prefixArr = new int[arr.length];

        prefixArr[0] = arr[0];
        for (int i = 1; i < prefixArr.length; i++) {

            prefixArr[i] = prefixArr[i - 1] + arr[i];
        }

//        for(int i = 0; i < prefixArr.length; i++) {
//
//            System.out.print(prefixArr[i]+" ");
//        }

        for (int i = 0; i < arr.length; i++) {

            for (int j = i; j < arr.length; j++) {

                sum = i == 0 ? prefixArr[j] : prefixArr[j] - prefixArr[i - 1];
                System.out.println("\n sum of sub array :" + sum);
                if (sum > max) {
                    max = sum;
                }
            }
        }
        System.out.println("maximum sum of sub array is : " + max);


    }
}
