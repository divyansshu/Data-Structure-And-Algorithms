package arrays;

import java.util.Arrays;

public class PlusOne {

    public static int[] plusOne(int[] digits) {
        int n = digits.length;
        for (int i = n - 1; i >= 0; i--) {
            // If the current digit is less than 9, just increment it and return the array
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
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
        int[] digits = {9,9};
        System.out.println(Arrays.toString(plusOne(digits)));

    }
    
}
