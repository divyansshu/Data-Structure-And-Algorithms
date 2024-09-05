package Algorthims.Searching;

public class BinarySearch {

    public static boolean search(int[] arr, int key) {

        int i = 0;
        int j = arr.length - 1;

        while(i<=j) {

            int mid = (i+j)/2;

            if(arr[mid] == key)
                return true;

            else if(arr[mid] < key)
                i = mid+1;

            else
                j = mid-1;
        }

        return false;
    }
    public static void main(String[] args) {

        int[] arr = {1,2,3,4,5,6,7,8,9};

        boolean check = search(arr, 1);

        if(check == true)
            System.out.println("true");
        else
        System.out.println("false");
    }
}
