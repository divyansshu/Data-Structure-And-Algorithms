package Strings;


public class Reverse2 {

    public static String  reverse(String str) {

        String str2 = "";

        for(int i = 0; i< str.length(); i++) {
            str2 = str.charAt(i) + str2;
        }

        return str2;
    }
    public static void main(String[] args) {

        String str= "hello";

        String str2 = (reverse(str));
        System.out.println(str2);
    }
}
