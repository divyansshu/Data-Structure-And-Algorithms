package Algorthims.sorting;

import java.util.Arrays;

public class MergeSort {

    public static int[] mergeAndsort(int[] arr) {

        //base case
        if(arr.length == 1) {
            return arr;
        }

        int mid = arr.length/2;

        int[] left = mergeAndsort(Arrays.copyOfRange(arr, 0, mid));
        int[] right = mergeAndsort(Arrays.copyOfRange(arr, mid, arr.length));

        return merge(left, right);
    }
  
    private static int[] merge(int[] first, int[] second) {
        
        int i = 0, j = 0, k = 0;
        int[] sortedArr = new int[first.length + second.length];

        while(i < first.length && j < second.length) {
            if(first[i] < second[j]) {
                sortedArr[k++] = first[i++];
            }
            else {
                sortedArr[k++] = second[j++];
            }
        }

        while(i < first.length) {
            sortedArr[k++] = first[i++];
        }

        while (j < first.length) {
            sortedArr[k++] = second[j++];
        }

        return sortedArr;
    }

    public static void main(String[] args) {

        int[] arr = {8,3,4,12,5,6};

        System.out.println("Array before merge sort");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }

        int[] sortedArr = mergeAndsort(arr);

        System.out.println("\nArray after merge sort");
        for(int i = 0; i < sortedArr.length; i++) {
            System.out.print(sortedArr[i]+ " ");
        }
        
    }
    
}
