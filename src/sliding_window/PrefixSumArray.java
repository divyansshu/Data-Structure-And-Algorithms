package sliding_window;

public class PrefixSumArray {

    //function to create a prefix sum array
    public static int[] prefix_arr(int[] arr) {
        int[] prefixArr = new int[arr.length];

        //approach 1
        // int k = 0, sum = 0;
        // for(int i = 0; i < arr.length; i++) {
        //     sum += arr[i];
        //     prefixArr[k] = sum;
        //     k++;
        // } 
        
        //approach 2
        prefixArr[0] = arr[0];
        for (int i = 1; i < prefixArr.length; i++) {
            prefixArr[i] = prefixArr[i - 1] + arr[i];
        }

        return prefixArr;   
       
    }


    //function to return maximum sum of subarray from all the subarrays
    public static int maxSum_subArray(int[] arr ,int[] prefixArr) {
        int sum = 0;
        int max = Integer.MIN_VALUE;

        for (int i = 0; i < arr.length; i++) {

            for (int j = i; j < arr.length; j++) {

                sum = i == 0 ? prefixArr[j] : prefixArr[j] - prefixArr[i - 1];
                System.out.println("\n sum of sub array :" + sum);
                if (sum > max) {
                    max = sum;
                }
            }
        }
        return max;
    }

    public static void displayArr(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();

    }

    public static void main(String[] args) {

        int[] arr = { 10, 4, 16, 20 };
        System.out.println("original array: ");
        displayArr(arr);

        //prefix array
        int[] prefixArr = prefix_arr(arr);
        System.out.println("prefix array: ");
        displayArr(prefixArr);
        
        System.out.println("maximum sum of sub array is : " + maxSum_subArray(arr, prefixArr));
        
    }
}
