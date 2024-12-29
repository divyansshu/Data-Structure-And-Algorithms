package BackTracking.BackTrackingOnArrays;

public class Example {

    public static void operations(int[] arr, int index) {
        if(index == arr.length) return;

        arr[index] = index + 1;
        operations(arr, index+1);
        arr[index] = arr[index] - 2;
    }
    public static void main(String[] args) {
        int[] arr = new int[5];
        operations(arr, 0);
        for(int A: arr) {
            System.out.print(A+" ");
        }
        
    }
    
}
