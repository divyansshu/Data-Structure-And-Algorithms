package arrays;

public class SecondLargestNumber {

    public static int find(int[] arr) {

        int max = arr[0];
        int max2 = 0;
        for(int i = 1; i < arr.length; i++) {
            if(max < arr[i]){
                max2 = max;
                max = arr[i];
            }
        }

//        max2 = arr[0];
//        for(int i = 1; i < arr.length; i++) {
//            if(arr[i] < max) {
//                if(arr[i] > max2) {
//                    max2 = arr[i];
//                }
//            }
//        }
        return max2;
    }
    public static void main(String[] args) {

        int[] arr = {10,30,24,40,35,45};

        System.out.println(find(arr));
    }
}
