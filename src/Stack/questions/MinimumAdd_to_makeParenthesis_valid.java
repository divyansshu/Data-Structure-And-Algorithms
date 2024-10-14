package Stack.questions;

import java.util.Stack;

//program to return minimum number of parenthesis required to balance the string
public class MinimumAdd_to_makeParenthesis_valid {
    
    public static int minAddToMakeValid(String s) {

        Stack<Character> S = new Stack<Character>();

        for (int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == ')') {
                if(!S.isEmpty() && S.peek() == '(') S.pop();
                else S.push(s.charAt(i));
            }
            else 
                S.push(s.charAt(i));
            }
        return S.size();    
    }
    public static void main(String[] args) {
        String s = "())";
        System.out.println(minAddToMakeValid(s));
        
    }
    
}
