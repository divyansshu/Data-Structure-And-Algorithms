package arrays;

import java.util.Arrays;

public class ArraySum {

    // Method to add two arrays representing numbers
    public static int[] addArrays(int[] A, int[] B) {

        int n = A.length; // Length of array A
        int m = B.length; // Length of array B

        int carry = 0; // Initialize carry to 0
        int size = Math.max(n, m); // Determine the size of the result array
        int[] C = new int[size + 1]; // Create result array with an extra space for carry

        int index = 0; // Initialize index to 0
        // Loop through both arrays until the end of the longer array
        while (index < n || index < m) {

            // Get the current digit from A or 0 if index is out of bounds
            int digitA = (index < n) ? A[index] : 0;
            // Get the current digit from B or 0 if index is out of bounds
            int digitB = (index < m) ? B[index] : 0;

            // Calculate the sum of the current digits and carry
            int sum = digitA + digitB + carry;
            
            // Store the last digit of the sum in the result array
            C[index] = sum % 10;
            // Update carry with the remaining part of the sum
            carry = sum / 10;

            index++; // Move to the next index
        }

        // If there is a carry left, store it in the result array
        if (carry > 0) {
            C[index++] = carry;
        }

        // Create the final result array with the correct size
        int[] finalResult = new int[index];
        // Reverse the result array to get the correct order
        for (int i = 0; i < index; i++) {
            finalResult[i] = C[index - i - 1];
        }

        return finalResult; // Return the final result array
    }

    public static void main(String[] args) {

        int[] A = { 3, 4, 2 }; // First number represented as an array
        int[] B = { 4, 6, 5 }; // Second number represented as an array

        // Print the result of adding the two arrays
        System.out.println(Arrays.toString(addArrays(A, B)));

    }

}
