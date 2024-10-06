package Stack.questions;

import java.util.Stack;

// import Stack.Implementation.UsingArrays.Stack;

public class Postfix_to_Infix {

    public static boolean isOperand(char c) {

        if(('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z') || ('0' <= c && c <= '9')) return true;

        else return false;

    }
    public static String convertToInfix(String exp) {

        Stack<String> s = new Stack<String>(); 

        for(int i = 0; i < exp.length(); i++) {
            if(isOperand(exp.charAt(i))) {
                s.push(String.valueOf(exp.charAt(i)));
            }

            else {
                String op1 = s.peek();
                s.pop();
                String op2 = s.peek();
                s.pop();
                s.push("(" + op2 + exp.charAt(i) + op1 + ")");
            }
        }
        
        return s.peek();
    }
    public static void main(String[] args) {
        
        String exp = "823^/23*+51*-";
        System.out.println(convertToInfix(exp));
    }
    
}
