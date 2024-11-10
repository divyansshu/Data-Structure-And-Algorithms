package queue.questions;

import java.util.HashMap;
import java.util.Queue;

public class First_Unique_Character_inString {

    /*
     * Time Complexity: (O(n)), where n is the length of the string. This is because
     * we iterate through the string twice.
     * Space Complexity: (O(1)), since the HashMap will store at most 26 characters
     * (assuming the input string contains only lowercase English letters).
     */

      public static int firstUniqChar(String s) {
      
        // Create a HashMap to store the frequency of each character
        HashMap<Character, Integer> charCount = new HashMap<>();
        
        // First pass: count the frequency of each character
        for(int i = 0; i < s.length(); i++) {
            charCount.put(s.charAt(i), charCount.getOrDefault(s.charAt(i), 0) + 1);
        }

        // Second pass: find the first unique character
        for(int i = 0; i < s.length(); i++) {
            if(charCount.get(s.charAt(i)) == 1) return i;
        }

        // If no unique character is found, return -1
        return -1;
               
    }
    public static void main(String[] args) {
        String s = "loveleetcode";

        System.out.println(firstUniqChar(s));

    }
    
}
