package Strings;

public class CountVowelsAndConsonants {

    public static void count(String str) {

        int vowels = 0;
        int consonants = 0;

        for(int i = 0; i < str.length(); i++) {

            if(str.charAt(i) == 'a' || str.charAt(i) == 'e' || str.charAt(i) == 'i' || str.charAt(i) == 'o' || str.charAt(i) == 'u'){
                vowels++;
            }
            else
                consonants++;
        }

        System.out.println("number of vowels and consonants in "+ str+" is "+ vowels+" and "+ consonants);
    }
    public static void main(String[] args) {

        String str = "technology";
        count(str);
    }
}
