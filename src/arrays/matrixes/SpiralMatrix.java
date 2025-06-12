package arrays.matrixes;

import java.util.ArrayList;
import java.util.List;

public class SpiralMatrix {
    public static List<Integer> spiralPrinting(int[][] matrix) {

        ArrayList<Integer> arr = new ArrayList<>();

        int left = 0;
        int right = matrix[0].length;
        int top = 0;
        int bottom = matrix.length;

        while(left < right && top < bottom) {

            //prints the top row elements
            for(int i = left; i < right; i++) {
                arr.add(matrix[top][i]);
            }
            top += 1;

            //check if it is only one row matrix
            if(!(top < bottom)) break;
            
            //prints the last column elements
            for (int i = top; i < bottom; i++) {
                arr.add(matrix[i][right-1]);
            }
            right -= 1;

            //check if it is one column matrix
            if(!(left < right)) break;

           // prints the last row elements
            for (int i = right-1; i >= left; i--) {
                arr.add(matrix[bottom-1][i]);
            }
            bottom -= 1;

            //prints the first column matrix
            for (int i = bottom - 1; i >= top; i--) {
                arr.add(matrix[i][left]);
            }
            left += 1;
        }
        
        return arr;

    }
    public static void main(String[] args) {
        int[][] matrix = {{1,2,3,4},{5,6,7,8},{9,10,11,12}};
        // int[][] arr = {{1,2,3,4}};
        // int[][] arr = {{1},{2},{3},{4}};

        System.out.println(spiralPrinting(matrix));
    }
    
}
