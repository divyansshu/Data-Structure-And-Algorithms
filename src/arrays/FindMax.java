package arrays;

import org.w3c.dom.ls.LSOutput;

import java.util.Scanner;

import static java.lang.Math.max;

public class FindMax {
    public static void main(String[] args) {
        System.out.println("Enter the size of an array");
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
         int[] arr = new int[n];
        System.out.println("Enter the elements of an array");
        for(int i = 0; i < n; i++) {
          arr[i] = sc.nextInt();
        }

        int max = 0;
        for(int i = 0; i < n; i++) {

            System.out.print(arr[i]+" ");
//            if (arr[i] > max) {
//                max = arr[i];
//            }
            if(i+1 < n) {
                max = max(arr[i], arr[i+1]);
            }

        }
        System.out.println("maximum element of an array is: " +max);


    }

}
