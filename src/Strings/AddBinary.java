package Strings;

public class AddBinary {
    /*
     * The current implementation of the addBinary method converts the binary
     * strings to integers, performs the addition using bitwise operations, and then
     * converts the result back to a binary string. However, this approach may not
     * handle very large binary strings correctly due to integer overflow.
     */
    public static String addBinary(String x, String y) {
        int a = Integer.parseInt(x,2);
        int b = Integer.parseInt(y,2);

        while (b != 0) {
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }

        return Integer.toBinaryString(a);
    }

    /*
     * This implementation handles binary addition directly on the strings and
     * avoids potential issues with integer overflow.
     * time complextiy: O(n)
     * space complexity: O(n)
     */
    public static String addBinary_2(String x, String y) {
        StringBuffer result = new StringBuffer();
        int i = x.length() - 1;
        int j = y.length() - 1;
        int carry = 0;

        while(i >= 0 || j >= 0 || carry != 0) {
            int bit1 = (i >= 0) ? x.charAt(i) - '0' : 0;
            int bit2 = (j >= 0) ? y.charAt(i) - '0' : 0;

            int sum = bit1 + bit2 + carry;
            result.append(sum % 2);
            carry = sum /2;
        }

        return result.reverse().toString();
    }
    public static void main(String[] args) {
        String a = "1010";
        String b = "1011";    

        System.out.println(addBinary(a,b));
        System.out.println(addBinary_2(a, b));
    }
    
}
