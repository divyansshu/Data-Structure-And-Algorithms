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

    /*
     * time complexity: O(n)
     * space complextiy: O(1)
     */
    public static int lengthOfLastWord_2(String s) {
        int len = s.length() - 1;
        int count = 0;

        while(len >= 0 && s.charAt(len) == ' ') {
            len--;
        }

        while(len >= 0 && s.charAt(len) != ' ') {
            count++;
            len--;
        }

        return count;
    }
    public static void main(String[] args) {
        String s = "   fly me   to   the moon     ";
        System.out.println(lengthOfLastWord(s.trim()));
        System.out.println(lengthOfLastWord_2(s));
        
    }
    
}
