package Strings;

public class LongestCommonPrefix {

    /*
     * time complexity: (m * n) where 𝑛 is the number of strings and 𝑚 is the
     * length of the shortest string.
     * space complexity: (1)
     */

    public static String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return "";
        }

        // Find the shortest string in the array
        String shortest = strs[0];
        for (String str : strs) {
            if (str.length() < shortest.length()) {
                shortest = str;
            }
        }

        // Compare characters of the shortest string with all other strings
        for (int i = 0; i < shortest.length(); i++) {
            char c = shortest.charAt(i);
            for (String str : strs) {
                if (str.charAt(i) != c) {
                    return shortest.substring(0, i);
                }
            }
        }

        return shortest;
    }

    public static void main(String[] args) {
        String[] strs = { "flower", "flow", "flight" };

        System.out.println(longestCommonPrefix(strs));
    }

}
