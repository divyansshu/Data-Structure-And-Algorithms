package Strings;

public class LengthOfLastWord {

    /*
     * time complexity: O(n)
     * space complextiy: O(n)
     */
    public static int lengthOfLastWord(String s) {

        int count = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                count = 0;
            } else {
                count++;
            }
        }
        return count;
    }
    public static void main(String[] args) {
        String s = "   fly me   to   the moon     ";
        System.out.println(lengthOfLastWord(s.trim()));
        
    }
    
}
