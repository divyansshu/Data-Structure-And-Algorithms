package Strings;

public class Reverse {

    public static String[] reverse(String[] str) {
        int j = str.length-1;

        int i = 0;
        while(i <= j) {

            String temp = str[i];
            str[i] = str[j];
            str[j] = temp;
            i++;
            j--;
        }

        return str;
    }


    public static void main(String[] args) {

        String[] str = {"H","e","l","l","o"};
       String[] str2=  reverse(str);
        for(int i = 0; i < str.length; i++) {
            System.out.print(str2[i]);
        }


    }
}
