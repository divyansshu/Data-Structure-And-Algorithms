package recursion;

public class GridTraveller {

    public static int fib(int term) {
        if(term < 1) return -1;
        if(term == 1) return 0;
        if(term ==2) return 1;
        return fib(term-1) + fib(term-2);

    }

    //directions: downward or rightward only
    //time complexity: O(2^(n+m))
    public static int gridTraveller(int n, int m) {

        int[][] dp = new int[n+1][m+1];
        dp[1][1] = 1;

        if(m<0|| n<0) return -1; //out of bounds

        if(m == 0 || n == 0) return 0; //there are no ways to travel(out of bounds)
        if(m == 1 || n == 1) return 1; // there is exactly one wat to travel (stay in place)

        //no.of ways(downward) + no.of ways(rightward)
        return gridTraveller(n-1, m) + gridTraveller(n, m-1);
        

    }
    public static void main(String[] args) {
        // System.out.println(fib(50));

        
        System.out.println(gridTraveller(3, 3));
    }
    
}
