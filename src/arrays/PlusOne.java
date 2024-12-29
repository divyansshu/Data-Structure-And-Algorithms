package arrays;

import java.util.Arrays;

public class PlusOne {

    public static int[] plusOne(int[] digits) {
        int n = digits.length;

        //skip leading zeroes
        int start = 0;
        while(start < n && digits[start] == 0) {
            start++;
        }
        //if all digits are zeroes, return [1]
        if(start == n) {
            return new int[]{1};
        }

        for (int i = n - 1; i >= start; i--) {
            // If the current digit is less than 9, just increment it and return the array
            if (digits[i] < 9) {
                digits[i]++;
                return Arrays.copyOfRange(digits, start, n);
            }
            // If the current digit is 9, it becomes 0
            digits[i] = 0;
        }
        // If all digits are 9, we need to add a leading 1
        int[] newNumber = new int[n + 1];
        newNumber[0] = 1;
        return newNumber;
    }
    public static void main(String[] args) {
        int[] digits = { 0, 3, 7, 6, 4, 0, 5, 5, 5};
        int[] digits2 = { 0,0,1,2 };
        System.out.println(Arrays.toString(plusOne(digits)));
        System.out.println(Arrays.toString(plusOne(digits2)));

    }
}
