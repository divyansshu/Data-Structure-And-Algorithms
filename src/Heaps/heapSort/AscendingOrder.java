package Heaps.heapSort;

//in heap sort to print elements in ascending order
//first convert the array into max heap
//then swap the largest(root) element with the last(minimum) element
public class AscendingOrder {

    public static void heapify(int[] arr, int i, int size) {
        int maxIndx = i;
        int leftIndx = 2*i + 1;
        int rightIndx = 2*i + 2;

        if(leftIndx < size && arr[leftIndx] > arr[maxIndx]) {
            maxIndx = leftIndx;
        }
        if(rightIndx < size && arr[rightIndx] > arr[maxIndx]) {
            maxIndx = rightIndx;
        }

        if(maxIndx != i) {
            int temp = arr[i];
            arr[i] = arr[maxIndx];
            arr[maxIndx] = temp;

            heapify(arr, maxIndx, size);
        }
    }
    public static void maxHeap(int[] arr) {
        //build maxheap
        int n = arr.length;
        for(int i = n/2; i >= 0; i--) {
            heapify(arr, i, n);
        }

        //step 2: push the largest element at last of heap
        for(int i = n -1; i > 0; i--) {
            //swap largest element with the first element
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            heapify(arr, 0, i);
        }
    }
    public static void main(String[] args) {
        int[] arr = {1,2,4,6,5,3,9,8 };

        maxHeap(arr);

        for(int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]+" ");
        }
    }
}
