package Algorthims.sorting;

import java.util.Arrays;

public class MergeSort {

    // Method to perform merge sort and return a sorted array
    public static int[] mergeAndsort(int[] arr) {

        // Base case: if the array has only one element, it is already sorted
        if(arr.length == 1) {
            return arr;
        }

        // Find the middle index of the array
        int mid = arr.length / 2;

        // Recursively sort the left and right halves of the array
        int[] left = mergeAndsort(Arrays.copyOfRange(arr, 0, mid));
        int[] right = mergeAndsort(Arrays.copyOfRange(arr, mid, arr.length));

        // Merge the sorted halves and return the sorted array
        return merge(left, right);
    }
  
    // Helper method to merge two sorted arrays into one sorted array
    private static int[] merge(int[] first, int[] second) {
        
        int i = 0, j = 0, k = 0;
        int[] sortedArr = new int[first.length + second.length];

        // Merge elements from both arrays in sorted order
        while(i < first.length && j < second.length) {
            if(first[i] < second[j]) {
                sortedArr[k++] = first[i++];
            } else {
                sortedArr[k++] = second[j++];
            }
        }

        // Copy any remaining elements from the first array
        while(i < first.length) {
            sortedArr[k++] = first[i++];
        }

        // Copy any remaining elements from the second array
        while (j < second.length) {
            sortedArr[k++] = second[j++];
        }

        return sortedArr;
    }

    // Method to perform in-place merge sort without creating extra arrays
    public static void mergeAndsortInplace(int[] arr, int start, int end) {

        // Base case: if the subarray has only one element, it is already sorted
        if (end - start == 1) {
            return;
        }

        // Find the middle index of the subarray
        int mid = (start + end) / 2;

        // Recursively sort the left and right halves of the subarray
        mergeAndsortInplace(arr, start, mid);
        mergeAndsortInplace(arr, mid, end);

        // Merge the sorted halves in place
        mergeInplace(arr, start, end, mid);
    }

    // Helper method to merge two sorted subarrays in place
    private static void mergeInplace(int[] arr, int start, int end, int mid) {

        int i = start, j = mid, k = 0;
        int[] sortedArr = new int[end - start];

        // Merge elements from both subarrays in sorted order
        while (i < mid && j < end) {
            if (arr[i] < arr[j]) {
                sortedArr[k++] = arr[i++];
            } else {
                sortedArr[k++] = arr[j++];
            }
        }

        // Copy any remaining elements from the left subarray
        while (i < mid) {
            sortedArr[k++] = arr[i++];
        }

        // Copy any remaining elements from the right subarray
        while (j < end) {
            sortedArr[k++] = arr[j++];
        }

        // Copy the sorted elements back to the original array
        for(int x = 0; x < sortedArr.length; x++) {
            arr[start + x] = sortedArr[x];
        }
    }

    public static void main(String[] args) {

        int[] arr = {8, 3, 4, 12, 5, 6};

        // Print the array before sorting
        System.out.println("Array before merge sort");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }

        // Perform in-place merge sort
        mergeAndsortInplace(arr, 0, arr.length);

        // Print the array after sorting
        System.out.println("\nArray after merge sort");
        System.out.println(Arrays.toString(arr));
    }
}
