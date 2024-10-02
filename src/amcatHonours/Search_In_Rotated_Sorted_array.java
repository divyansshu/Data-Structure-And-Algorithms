package amcatHonours;

public class Search_In_Rotated_Sorted_array {

    public static int pivot(int[] arr) {
         int start = 0;
        int end = arr.length - 1;

        while(start <= end) {
            int mid = (start+end)/2;

            if(mid < end && arr[mid] > arr[mid+1]) return mid;
            
            else if(mid > start && arr[mid] < arr[mid-1]) {
                return mid-1;
            }

            else if(arr[mid] <= arr[start]) {
                end = mid - 1;
            }
            else //arr[mid] >= arr[start]
             {
                start = mid + 1;

            }
        }
        return -1;
    }

    public static int search(int[] arr, int key) {

        int pivot = pivot(arr);

        //case1: 
        //array is not rotated, just do normal binary search
         if(pivot == -1) {
            return binarySearch(arr, key, 0, arr.length - 1);
        }

        //case2:
        else if(arr[pivot] == key) return pivot;     
        
        //case3:
        //if pivot is not -1
        else if(arr[0] > key) {
            return binarySearch(arr, key, pivot + 1, arr.length-1);
        }

        //case4:
        // if key > arr[0]
        else {
            return binarySearch(arr,key, 0, pivot - 1);
        }

    }

    public static int binarySearch(int[] arr,int key, int start, int end) {
        
        while(start <= end) {

            int mid = (start+end)/2;

            if(arr[mid] == key) return mid;
            else if (key > arr[mid]) start = mid + 1;
            else end = mid - 1;
        }
        return -1;
    }
    public static void main(String[] args) {
        int[] arr = {4,5,6,7,0,1,2};
        System.out.println(search(arr, 4));
    }
}
