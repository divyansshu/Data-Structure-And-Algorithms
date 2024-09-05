package Strings;

public class Occurrences {

    public static int occurrences(String str, char ch) {

        int count = 0;

        for(int i  = 0; i < str.length(); i++) {
            if(str.charAt(i) == ch) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {

        String str = "aabcdeaa";

        char ch = 'a';

        System.out.println(occurrences(str, ch));
    }
}
