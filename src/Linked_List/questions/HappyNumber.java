package Linked_List.questions;

public class HappyNumber {
    //using two pointers (slow and fast)

    /*
     * A happy number is a number defined by the following process:
     * Starting with any positive integer, replace the number by the sum of the
     * squares of its digits.
     * Repeat the process until the number equals 1 (where it will stay), or it
     * loops endlessly in a cycle which does not include 1.
     * Those numbers for which this process ends in 1 are happy.
     */

    public static boolean isHappy(int n) {

        int slow = n;
        int fast = n;

        do {
            slow = returnSquare(slow);
            fast = returnSquare(returnSquare(fast));
        }while(fast != slow);

        if(slow == 1) return true;
        return false;
    }

    public static int returnSquare(int num) {

        int sq = 0;

        while (num != 0) {
            int rem = num % 10;
            sq += rem * rem;
            num /= 10;
        }
        return sq;
    }

    public static void main(String[] args) {
        System.out.println(isHappy(2));

    }

}
