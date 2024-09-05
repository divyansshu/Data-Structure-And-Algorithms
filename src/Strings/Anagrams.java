package Strings;

import java.util.Arrays;

public class Anagrams {

    public static boolean anagrams(String str1, String str2) {

        if(str1.length() != str2.length())
            return false;

        char[] anag1 = str1.toCharArray();
        char[] anag2 = str2.toCharArray();

        Arrays.sort(anag1);
        Arrays.sort(anag2);


        boolean isAnagram = Arrays.equals(anag1,anag2);

        if(isAnagram == true)
            return true;

        return false;
    }

    public static void main(String[] args) {

        String str1 = "cat";
        String str2 = "bat";

        System.out.println(anagrams(str1, str2));
    }
}
