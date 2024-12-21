import java.util.Scanner;

public class UglyNumber {

    public static boolean isUgly(int num) {
        
        if(num <= 0) return false;

        int[] factors = {2,3,5};

        for(int factor: factors) {
            while(num % factor == 0) {
                num /= factor;
            }
        }
        return num == 1;
    }
    public static void main(String[] args) {
        
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter any Number");

            int num = sc.nextInt();
            System.out.println("Is "+ num +" an ugly number: "+ isUgly(num));
        }
    }
    
}
