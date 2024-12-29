package BackTracking.BackTrackingOnArrays;

public class StringPermutations {
    
    // Method to find all permutations of a given string
    public static void findPermutations(String str, String result) {

        // Base case: if the input string is empty, print the result
        if(str.length() == 0) {
            System.out.println(result);
            return;
        }

        // Loop through the string
        for(int i = 0; i < str.length(); i++) {
            // Get the current character
            char curr = str.charAt(i);
            // Create a new string by removing the current character
            String newString = str.substring(0, i) + str.substring(i+1);
            // Recursively call the method with the new string and the current result
            findPermutations(newString, result + curr);
        }
    }
    
    public static void main(String[] args) {
        // Input string
        String str = "abc";
        // Call the method to find permutations with an empty result string
        findPermutations(str, new String(""));
    }
    
}
