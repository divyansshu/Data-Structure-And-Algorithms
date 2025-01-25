package Strings;

/*
 * Return the number of substrings in s which starts with vowel and end with consonants or vice-versa.
 * Return the count of substring modulo 10^9 + 7.
 */
public class Vowel_and_Consonant_substring {

    // Helper method to check if a character is a vowel
    private static boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    // Method to count the number of valid substrings
    public static int subStringsCount(String s) {

        int vowelsCount = 0, consonantsCount = 0, result = 0;
        int mod = 1000000007;

        // Iterate through each character in the string
        for (char c : s.toCharArray()) {
            if (isVowel(c)) {
                // If the character is a vowel, increment the vowel count
                vowelsCount++;
                // Add the number of consonants seen so far to the result
                result += consonantsCount;
            } else {
                // If the character is a consonant, increment the consonant count
                consonantsCount++;
                // Add the number of vowels seen so far to the result
                result += vowelsCount;
            }
        }
        // Take the result modulo 10^9 + 7
        result %= mod;
        return (int) result;
    }

    public static void main(String[] args) {
        String s = "abcde";
        // Print the count of valid substrings
        System.out.println(subStringsCount(s));
    }

}
