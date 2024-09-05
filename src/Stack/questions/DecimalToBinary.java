package Stack.questions;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class DecimalToBinary {

    public static Stack<Integer> conversion(int n) {

//        Queue<Integer> q = new LinkedList<>();

        Stack<Integer> s = new Stack<>();
        while(n != 1) {

            s.add(n % 2);
            n /= 2;
        }
        s.add(1);
        return s;
    }
    public static void main(String[] args) {

//        Queue<Integer> q1 = new LinkedList<>();
        Stack<Integer> s1 = new Stack<>();
       s1 =  conversion(4);
       while (!s1.isEmpty()) {

           System.out.print(s1.peek()+" ");
           s1.pop();
       }
    }
}
