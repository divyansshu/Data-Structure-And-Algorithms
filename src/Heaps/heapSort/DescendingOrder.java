package Heaps.heapSort;

//in heap sort to print elements in descending order
//first convert the array into min heap
//then swap the minimum(root) element with the last(largest) element
public class DescendingOrder {

    public static void heapify(int[] arr, int i, int size) {
        int minIndx = i;
        int leftIndx = 2*i + 1;
        int rightIndx = 2*i + 2;

        if(leftIndx < size && arr[leftIndx] < arr[minIndx]) {
            minIndx = leftIndx;
        }
        if(rightIndx < size && arr[rightIndx] < arr[minIndx]) {
            minIndx = rightIndx;
        }

        if(minIndx != i) {
            int temp = arr[i];
            arr[i] = arr[minIndx];
            arr[minIndx] = temp;

            heapify(arr, minIndx, size);
        }
    }
    public static void minHeap(int[] arr) {
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

        minHeap(arr);

        for(int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]+" ");
        }
    }
}

