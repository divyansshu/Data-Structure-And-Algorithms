package HashMaps.implementation;

import java.util.HashMap;
import java.util.Map;

public class Maps {

    public static void main(String[] args) {

        HashMap<String, Integer> map = new HashMap<>();

        map.put("India", 140);
        map.put("china", 150);
        map.put("USA", 145);
        map.put("India", 140); // maps does not take duplicate values

        System.out.println(map);// to display all keys and values of map

        System.out.println();

        //we can access keys,values of map like this
        for (Map.Entry<String, Integer> e : map.entrySet()) {
            System.out.println(e.getKey());
            System.out.println(e.getValue());
        }
        System.out.println();

        map.remove("India"); // to remove or delete key,value from map
        System.out.println(map);

        System.out.println();

        for (Map.Entry<String, Integer> e : map.entrySet()) {
            System.out.println(e.getKey());
            System.out.println(e.getValue());
        }
        
    }
}
