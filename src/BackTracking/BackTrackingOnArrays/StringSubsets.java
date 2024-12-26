package BackTracking.BackTrackingOnArrays;

public class StringSubsets {

    
    // This method finds and prints all subsets of the given string.
    // It uses a recursive approach to generate subsets.  
    public static void findSubsets(String str, String ans, int i) {
        
        // Base case: If the current index is equal to the length of the string,
        // print the current subset and return.
        if(i == str.length()) {
            System.out.println(ans);
            return;
        }

        // Recursive case 1: Include the current character in the subset.
        findSubsets(str, ans + str.charAt(i), i + 1);

        // Recursive case 2: Exclude the current character from the subset.
        findSubsets(str, ans, i + 1);
    }
    public static void main(String[] args) {
        String str = "abc";
        findSubsets(str, "", 0);
    }
}
