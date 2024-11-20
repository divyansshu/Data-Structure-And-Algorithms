package Algorthims.sorting;

import java.util.Arrays;

public class QuickSort {

    // Main method to perform quick sort
    public static void quickSort(int[] nums, int s, int e) {

        // Base condition to end recursion
        if(s >= e) return;

        // Find the middle index and pivot element
        int mid = s + (e - s) / 2;
        int pivot = nums[mid];

        int left = s;
        int right = e;

        // Partition the array around the pivot
        while(left <= right) {
            while(nums[left] < pivot) left++;
            while(nums[right] > pivot) right--;

            if(left <= right) {
                // Swap elements
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left++;
                right--;
            } 
        }
        // Recursively sort the left and right subarrays
        quickSort(nums, s, right);
        quickSort(nums, left, e);
    }

    public static void main(String[] args) {
        int[] nums = {5,1,1,2,0,0};
        System.out.println("Quick Sort Algorithm");

        // Perform quick sort on the array
        quickSort(nums, 0, nums.length - 1);

        // Print the sorted array
        System.out.println(Arrays.toString(nums));
    }
    
}
