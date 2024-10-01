package arrays;

import java.util.Arrays;

public class Maximum_numbers_Of_ones {


    /**
      Brute force method
    public static int[] rowAndMaximumOnes(int[][] mat) {

        int row = mat.length;
        int col = mat[0].length;
        int max_ones = 0;
        int count = 0;
        int index = 0;
        int[] arr = new int[2];

        for(int i = 0; i < row; i++ ) {
            count = 0;
            for(int j = 0; j < col; j++) {
                if(mat[i][j] == 1) {
                    count++;
                }
            }
            if(count > max_ones) {
                max_ones = count;
                index = i;
            }
        }
        arr[0] = index;
        arr[1] = max_ones;

        return arr;
    }
     **/

    public static void main(String[] args) {
        int[][] arr = {{0},{1},{1},{1},{0}};
        System.out.println(Arrays.toString(rowAndMaximumOnes(arr)));
    }
}
