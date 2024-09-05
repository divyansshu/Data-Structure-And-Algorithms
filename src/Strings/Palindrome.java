package Strings;

public class Palindrome {
    public static String  reverse(String str) {

        String str2 = "";

        for(int i = 0; i< str.length(); i++) {
            str2 = str.charAt(i) + str2;
        }

        return str2;
    }
    public static void main(String[] args) {

        String str= "NitiN";

        if(reverse(str).equals(str))
            System.out.println("palindrome");

        else
            System.out.println("Not palindrome");
    }
}
