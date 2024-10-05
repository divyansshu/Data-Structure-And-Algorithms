package arrays.sliding_window;

class ContainsDuplicate {

    public static boolean containsNearbyDuplicate(int[] arr, int k) {
        int i = 0;
        int j = arr.length - 1;

        while (i < j) {

            if (j > i) {
                if (arr[i] == arr[j]) {
                    if (Math.abs(i - j) <= k)
                        return true;
                    else
                        j--;
                } else {
                    j--;
                }
            } 
            else {
                j = arr.length - 1;
                i++;
            }
        }      
        return false;
    }
    public static void main(String[] args) {
        int arr[] = {1,0,1,1};
        System.out.println(containsNearbyDuplicate(arr,1));
    }
}