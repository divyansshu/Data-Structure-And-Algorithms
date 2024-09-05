package HashMaps.questions;

import java.util.HashMap;

public class ItineraryFromTickets {

    public static void findItinerary(HashMap<String,String> tickets) {

        //reversing the hashmap key = value, value = key
        HashMap<String, String> revTickets = new HashMap<>();
        for(String key: tickets.keySet()) {

            revTickets.put(tickets.get(key), key);
        }

        System.out.println(revTickets);
        System.out.println();

        //finding starting location
        String start="";
        for (String key: tickets.keySet()) {

            if(revTickets.containsKey(key) == false) {
                start = key;
            }
        }

        //printing the path form starting to end
        System.out.print(start);
        while(tickets.containsKey(start)) {
            System.out.print("->"+tickets.get(start));
            start = tickets.get(start);
        }

    }
    public static void main(String[] args) {

        HashMap<String, String> tickets = new HashMap<>();
        tickets.put("Chennai", "Bengaluru");
        tickets.put("Mumbai", "Delhi");
        tickets.put("Goa", "Chennai");
        tickets.put("Delhi", "Goa");

        System.out.println(tickets);
        System.out.println();

        findItinerary(tickets);
    }
}
