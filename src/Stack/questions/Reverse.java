package Stack.questions;

import java.util.Stack;

public class Reverse {

    public static void pushAtBottom(int data, Stack<Integer> s) {

        if(s.isEmpty()) {
            s.push(data);
            return;
        }
        int top = s.pop();
        pushAtBottom(data, s);
        s.push(top);
    }

    public static void reverse(Stack<Integer> s) {

        if(s.isEmpty())
            return;

        int top = s.pop();
        reverse(s);
        pushAtBottom(top, s);
    }

//    public static void reverse(Stack<Integer> s, Stack<Integer> s2) {
//
//        while(!s.isEmpty()) {
//            int top = s.peek();
//            s2.push(top);
//            s.pop();
//        }
//    }
    public static void main(String[] args) {
        Stack<Integer> s = new Stack<>();
        s.push(10);
        s.push(20);
        s.push(30);

//        Stack<Integer> s2 = new Stack<>();
        reverse(s);

        System.out.println("reversed stack");
        while(!s.isEmpty()) {
            System.out.println(s.peek());
            s.pop();
        }

    }
}
