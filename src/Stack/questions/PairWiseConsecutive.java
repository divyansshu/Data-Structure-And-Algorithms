package Stack.questions;

import java.util.Stack;

public class PairWiseConsecutive {
    public static boolean pairWiseConsecutive(Stack<Integer> st)
    {
        Stack<Integer> aux = new Stack<>();
        boolean result = true;

        while(!st.isEmpty()) {

            aux.push(st.peek());
            st.pop();
        }

        while(aux.size() > 1) {

            int top1 = aux.peek();
            aux.pop();
            int top2 = aux.peek();
            aux.pop();

            if(Math.abs(top1 - top2) != 1) {
                result =  false;
            }

            st.push(top1);
            st.push(top2);
        }

        if(aux.size() == 1) {
            st.push(aux.peek());
        }
        return result;
    }

    public static void main(String[] args) {

        Stack<Integer> st = new Stack<>();
        st.push(6);
        st.push(5);
        st.push(4);
        st.push(3);
        st.push(2);
        st.push(3);

        System.out.println(pairWiseConsecutive(st));
    }
}
