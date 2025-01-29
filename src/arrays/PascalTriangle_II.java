package arrays;

import java.util.ArrayList;
import java.util.List;

public class PascalTriangle_II {
    
    // Method to get the specific row of Pascal's Triangle
    public static List<Integer> getrow(int rowIndex) {

        List<Integer> row = new ArrayList<>();
        
        // Initialize the row with the first element as 1
        row.add(1);

        // Loop to generate each row up to the given rowIndex
        for(int i = 1; i <= rowIndex; i++) {
            // Update the row elements from the end to the start
            for(int j = row.size()-1; j > 0; j--) {
               row.set(j, row.get(j) + row.get(j-1));
            }
            // Add 1 at the end of the row for the next element
            row.add(1);
        }
        return row;
    }

    public static void main(String[] args) {

        int rowIndex = 3;
        // Print the row at the given rowIndex
        System.out.println(getrow(rowIndex));
        
    }
    
}
