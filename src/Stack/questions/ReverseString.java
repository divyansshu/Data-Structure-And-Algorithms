package Stack.questions;

import java.util.Stack;

public class ReverseString {

    public static String reverse(String S) {

        Stack<String> s = new Stack<>();

        for (int i = 0; i < S.length(); i++) {

            s.push(String.valueOf(S.charAt(i)));
        }
        S = "";
        while (!s.isEmpty()) {
            S += s.peek();
            s.pop();
        }
        return S;
    }

    public static void main(String[] args) {

        String strr = "GeeksForGeeks";
        System.out.println(reverse(strr));
        }
}
