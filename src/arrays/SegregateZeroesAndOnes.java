package arrays;

import java.util.Arrays;

public class SegregateZeroesAndOnes {

    public static int[] segregate_Zeroes_and_Ones(int[] A) {
        int i = 0;
        int j = A.length - 1;

        while (i < j) {

            if (A[i] == 0) i++;
            else if (A[j] == 1) j--;
            else // (A[i] == 1 && A[j] == 0)
            {
                A[i] = 0;
                A[j] = 1;
                i++;
                j--;
            }
        }
        return A;
    }
    public static void main(String[] args) {
        int[] A = {1,1,0,0,1,0,1,0,0,0};
        System.out.println(Arrays.toString(segregate_Zeroes_and_Ones(A)));
        
    }
    
}
