package Strings;

public class RemoveOccurrences {

    public static String removeOccurrences(String str, char ch) {

        for(int i = 0; i < str.length(); i++) {

            if(str.charAt(i) == ch) {
                str = str.replace("e", "");
            }
        }

        return str;
    }
    public static void main(String[] args) {

        String str = "Geeks";

        char ch = 'e';

        System.out.println(removeOccurrences(str, ch));
    }
}
