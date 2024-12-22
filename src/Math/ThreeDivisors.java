public class ThreeDivisors {

    public static boolean threeDivisors(int n) {
        int root = (int) Math.sqrt(n);
        
        if((root * root) != n) return false;

        if(root < 2) return false;

        for(int i = 2; i <= Math.sqrt(root); i++) {
            if(root % i == 0) return false;
        }
        return true;
    }
    public static void main(String[] args) {

        System.out.println(threeDivisors(81));
        
    }
    
}
