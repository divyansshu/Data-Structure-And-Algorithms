package Stack.questions;
import java.util.Stack;

public class ValidParenthesis {

    //function to check is brackets are balanced or not
    //time compexity: O(n)
    //space complexity: O(n)
    public static boolean isValid(String s) {
        Stack<Character> S = new Stack<Character>();
        int n = s.length() - 1;

        for (int i = 0; i <= n; i++) {
            //check if the character is an opening bracket
            if (s.charAt(i) == '(' || s.charAt(i) == '[' || s.charAt(i) == '{') {
                S.push(s.charAt(i));
                // System.out.println(S.peek());
            }

            else {
            
                // If it's a closing bracket, check if the stack is non-empty
                // and if the top of the stack is a matching opening bracket
                if (!S.isEmpty() &&
                 S.peek() == '(' && s.charAt(i) == ')' ||
                  S.peek() == '{' && s.charAt(i) == '}' ||
                   S.peek() == '[' && s.charAt(i) == ']') 
                   S.pop();
                else
                    return false; //umatched closing bracket
            }
        }

        //if stack is empty return true(balanced)
        //other wise false
        return S.isEmpty();

    }

   
    public static void main(String[] args) {
        String s = "()[]{}";

        if(isValid(s)) System.out.println("valid");
        else System.out.println("not valid");

    }
    
}
