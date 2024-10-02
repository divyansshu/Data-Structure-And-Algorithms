package arrays;


import java.util.Scanner;

public class SubArrays {

    public static void printSubArray(int[] arr) {
        int N = arr.length;
        for(int i = 0;  i<N; i++) {
            for (int j = i; j < N; j++) {
                for(int k = i; k <=j; k++) {
                    System.out.println(arr[k]+ " ");
                }
                System.out.println();
            }
            System.out.println();
        }
    }
    public static void subArraysUsingSW(int[] arr) {
        int N = arr.length;
        for( int window = 1; window<=N; window++) {
            for(int start = 0; start<=N; start++) {
                int end = (start+window) -1;
                for (int i = start; i <= end; i++) {
                    System.out.println(arr[i]+ " ");
                }
                System.out.println();
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr= new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        for (int i = 0; i < N; i++) {
            System.out.print(arr[i]+ " ");
        }

        printSubArray(arr);
        subArraysUsingSW(arr);
    }
}
