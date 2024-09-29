package HashMaps;

import java.util.HashMap;

public class map {
    public static void main(String[] args) {
        int[] nums = {3,1,3,3,2};
        int count = 0;

        HashMap<Integer,Integer> map = new HashMap<>();
        for( int i = 0; i < nums.length; i++) {
            map.put(count,nums[i]);

        }

        System.out.println(map);


    }
}
