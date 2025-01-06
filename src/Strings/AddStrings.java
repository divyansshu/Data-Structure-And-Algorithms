package Strings;

public class AddStrings {

    // Method to add two numeric strings
    public static String addStrings(String num1, String num2) {

        int i = num1.length() - 1; // Initialize pointer for num1 at the last character
        int j = num2.length() - 1; // Initialize pointer for num2 at the last character
        int carry = 0; // Initialize carry to 0
        StringBuilder result = new StringBuilder(); // StringBuilder to store the result

        // Loop until both strings are processed
        while (i >= 0 || j >= 0) {
            // Get the current digit of num1, or 0 if i is out of bounds
            int digit1 = (i >= 0) ? num1.charAt(i) - '0' : 0;
            // Get the current digit of num2, or 0 if j is out of bounds
            int digit2 = (j >= 0) ? num2.charAt(j) - '0' : 0;

            // Calculate the sum of the digits and the carry
            int sum = digit1 + digit2 + carry;
            // Append the last digit of the sum to the result
            result.append(sum % 10);
            // Update the carry
            carry = sum / 10;
            // Move to the next digit in num1
            i--;
            // Move to the next digit in num2
            j--;
        }
        // If there is a carry left, append it to the result
        if (carry > 0) {
            result.append(carry);
        }

        // Reverse the result to get the final sum and convert to string
        return result.reverse().toString();
    }

    public static void main(String[] args) {
        String num1 = "11"; // First number as string
        String num2 = "123"; // Second number as string

        // Print the result of adding num1 and num2
        System.out.println(addStrings(num1, num2));
    }
    
}
