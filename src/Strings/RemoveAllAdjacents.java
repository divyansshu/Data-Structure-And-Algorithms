package Strings;

import java.util.Stack;

public class RemoveAllAdjacents {

    /*
     * time complexity: O(n)
     * Space complexity: O(n)
     */
    public static String removeDuplicates(String s) {
        // Check if the input string is null or empty, return it as is
        if(s == null || s.length() == 0) return s;

        // Initialize a stack to keep track of characters
        Stack<Character> stack = new Stack<>();

        // Iterate through each character in the string
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            // If the stack is not empty and the current character is the same as the top of the stack, pop the stack
            if (!stack.isEmpty() && c == stack.peek()) {
                stack.pop();
            } else {
                // Otherwise, push the current character onto the stack
                stack.push(c);
            }
        }

        // Initialize a StringBuffer to build the result string
        StringBuffer result = new StringBuffer();
        // Pop all characters from the stack and append to the result
        while (!stack.isEmpty()) {
            result.append(stack.pop());
        }
        // Reverse the result string and return it
        return result.reverse().toString();
    }

    /*
     * time complexity: O(n)
     * Space complexity: The StringBuilder can potentially store all characters
     * of the input string in the worst case, which requires O(n) space.
     */
    public static String removeDuplicates_method2(String s) {
        // Check if the input string is null or empty, return it as is
        if(s == null || s.length() == 0) return s;

        // Initialize a StringBuilder to build the result string
        StringBuilder str = new StringBuilder();

        // Iterate through each character in the string
        for(char c: s.toCharArray()) {
            int len = str.length();

            // If the StringBuilder is not empty and the current character is the same as the last character in the StringBuilder, delete the last character
            if(len > 0 && c == str.charAt(len-1)) {
                str.deleteCharAt(len-1);
            } else {
                // Otherwise, append the current character to the StringBuilder
                str.append(c);
            }
        }
        // Return the result string
        return str.toString();
    }

    public static void main(String[] args) {
        // Test the methods with the input string "abbaca"
        String s = "abbaca";
        System.out.println(removeDuplicates(s)); // Output: "ca"
        System.out.println(removeDuplicates_method2(s)); // Output: "ca"
    }
}
