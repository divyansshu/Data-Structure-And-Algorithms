package arrays;

public class Minimum_in_sorted_rotated_array {

    public static int min_in_rotated_sorted_array(int[] arr) {
        int low = 0;
        int high = arr.length - 1;
        
        while(low < high) {

            if(arr[low] < arr[high]) {
                return low;
            }

           int mid = (low+high)/2;

            if(arr[mid] > arr[high]) {
                low = mid + 1;
            }
            else 
                high = mid;
            
        }
        return low;
    }
    public static void main(String[] args) {

        // rotated sorted array
        int[] arr= {4, 5, 6, 9, 0, 1, 2};
        int[] arr2 = {5,6,1,2,3,4};
 
        int min = min_in_rotated_sorted_array(arr2);
        System.out.println("minimum element in rotated sorted array is: "+ arr2[min]+ " at index "+ min);
    }
}
