package Strings;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;


public class Anagrams {

    /*
     * time complexity: O(n logn)
     * space complexity: O(n)
     */
    public static boolean anagrams(String str1, String str2) {

        if(str1.length() != str2.length())
            return false;

        char[] anag1 = str1.toCharArray();
        char[] anag2 = str2.toCharArray();

        Arrays.sort(anag1);
        Arrays.sort(anag2);

        /*
         * Sorting each string takes O(n log n) time, where n is the length of the
         * strings.
         * Comparing the two sorted arrays takes O(n) time.
         */

        return Arrays.equals(anag1,anag2);
   
    }
/*
 * time complexity: O(n)
 * space complexity: O(n)
 */
    public static boolean isAnagram(String s, String t) {
        
        // If lengths are different, they cannot be anagrams
        if (s.length() != t.length())
            return false;

        // Create a map to count characters in string s
        Map<Character, Integer> countMap = new HashMap<>();

        // Count characters in s
        for (char c : s.toCharArray()) {
            countMap.put(c, countMap.getOrDefault(c, 0) + 1);
        }

        // Subtract character counts based on string t
        for (char c : t.toCharArray()) {
            if (!countMap.containsKey(c))
                return false;
            countMap.put(c, countMap.get(c) - 1);
            if (countMap.get(c) == 0)
                countMap.remove(c);
        }

        // If the map is empty, s and t are anagrams
        return countMap.isEmpty();    
    }

    public static void main(String[] args) {

        String str1 = "cat";
        String str2 = "bat";

        System.out.println(anagrams(str1, str2));
        System.out.println(isAnagram(str1, str2));
    }
}
