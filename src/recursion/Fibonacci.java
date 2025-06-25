package recursion;

import java.util.Arrays;

public class Fibonacci {

    public static int fib(int[] sol, int n) {

        if(n == 0)
            return 0;

        if(n == 1)
            return 1;
        if(n == 2)
            return 1;

        if(sol[n] != -1) return sol[n];

        sol[n] = fib(sol, n-2) + fib(sol, n-1);

        return sol[n];

    }
    public static void main(String[] args) {

        int n = 45;
        int[] sol = new int[n+1];
        Arrays.fill(sol, -1);

//        for(int i = 0; i <= n; i++) {
            System.out.print(fib(sol, n));
//        }
    }
}
