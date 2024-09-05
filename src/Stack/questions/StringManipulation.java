package Stack.questions;

import java.util.Stack;

public class StringManipulation {

    public static int removeConsecutiveSame(String[] arr) {

        Stack<String> s = new Stack<>();

        for(int i = 0; i < arr.length; i++) {

            if(s.isEmpty())
                s.push(arr[i]);

            else {
                String str = s.peek();

                if(str.equals(arr[i]))
                    s.pop();
                else
                    s.push(arr[i]);
            }
        }
        return s.size();
    }

    public static void main(String[] args) {

        String[] arr = {"z", "abcd", "u", "aa", "abcde", "aa", "cc", "cc", "abc", "def"};

        System.out.println(removeConsecutiveSame(arr));
    }
}
