package arrays.sliding_window;


import java.util.Scanner;

public class SubArrays {

    //Brute force
    //printing total number of sub arrays 
    public static void printSubArray(int[] arr) {
        int N = arr.length;
        for(int i = 0;  i<N; i++) {
            for (int j = i; j < N; j++) {
                for(int k = i; k <=j; k++) {
                    System.out.print(arr[k]+ " ");
                }
                System.out.println();
            }
            System.out.println();
        }
    }

    // printing all sub arrays optimized method
    public static void subArraysUsingSW(int[] arr) {
        int N = arr.length - 1;
        for( int window = 1; window<=N; window++) {
            for(int start = 0; start<=N; start++) {
                int end = (start+window) - 1;
                if(end > N) return;
                for (int i = start; i <= end; i++) {
                    System.out.print(arr[i]+ " ");
                }
                System.out.println();
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the size of an array");
        int N = sc.nextInt();

        int[] arr= new int[N];

        System.out.println("Enter the elements of an array");
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        System.out.println("Array is: ");
        for (int i = 0; i < N; i++) {
            System.out.print(arr[i]+ " ");
        }
        System.out.println();

        // printSubArray(arr);
        subArraysUsingSW(arr);
    }
}
