package CodingNinjas;
import java.util.Arrays;

public class NinjaWantsHoliday {

    static String ninjaWantsHoliday(int n, int k, int []a) {
        // Write your code here.

        Arrays.sort(a);

        int count = 0;

        for(int i = 0; i < n; i++) {

            if(i + 1 < n) {

                if(a[i] == (a[i+1] - 1)) {

                    count++;
                    if(count  == k-1) {
                        return "YES";
                    }

                }

                else {
                    if(a[i] != (a[i+1] - 1) && count >= 1) {
                        count = 0;
                    }
                }
            }
        }
        return "NO";
    }

    public static void main(String[] args) {


        int[] a = {22, 4, 42, 45, 49, 47, 29, 11, 24, 27, 39, 36, 19, 14, 16, 31, 38, 44, 40, 46, 6, 28, 8, 20, 10, 5, 13, 48, 34, 2, 9, 26, 1, 41, 33, 17, 35, 7, 32, 18};
        System.out.println(ninjaWantsHoliday(40, 3, a));
    }
}
