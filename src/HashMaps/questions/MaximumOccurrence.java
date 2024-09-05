package HashMaps.questions;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class MaximumOccurrence {

    public static ArrayList<Integer> maximumOccurrence(int[] arr) {
        ArrayList<Integer> list = new ArrayList<>();
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < arr.length; i++) {

            if(map.containsKey(arr[i])) {

                map.put(arr[i], map.get(arr[i])+1);
            }
            else {
                map.put(arr[i], 1);
            }
        }

        for(int key: map.keySet()) {

            if(map.get(key) > (arr.length/3)) {
                list.add(key);
            }
        }
        return list;
    }
    public static void main(String[] args) {
//        int[] arr = {1,3,2,5,1,3,1,5,1,3,3};
          int[] arr = {1,2};
        System.out.println(maximumOccurrence(arr));
    }
}
