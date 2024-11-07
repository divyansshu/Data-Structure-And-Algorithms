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
    public static void main(String[] args) {
        String a = "1010";
        String b = "1011";    

        System.out.println(addBinary(a,b));
    }
    
}
