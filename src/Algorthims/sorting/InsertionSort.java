package Algorthims.sorting;

public class InsertionSort {

    public static void insertionSort(int[] arr) {

        for(int i = 1; i < arr.length; i++) {

            int key  = arr[i];
            int j = i-1;

            while(j >= 0 && arr[j] > key) {
                arr[j+1] = arr[j];
                j = j-1;
            }
            arr[j+1] = key;
        }
    }
    public static void main(String[] args) {

        int[] arr = {5,4,8,2,3,6,1,9,7};

        insertionSort(arr);

        for(int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]+ " ");
        }
    }
}
