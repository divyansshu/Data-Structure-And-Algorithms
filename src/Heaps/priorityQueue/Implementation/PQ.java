package Heaps.priorityQueue.Implementation;

import java.util.Comparator;
import java.util.PriorityQueue;

public class PQ {
    public static void main(String[] args) {
//priority Queue give priority in ascending order by default
//        PriorityQueue<Integer> pq = new PriorityQueue<>();

        //to give priority in descending order use comparator.reverseOrder()
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());

        //add in O(log n)
        pq.add(3);
        pq.add(4);
        pq.add(1);
        pq.add(7);
        pq.add(9);

        while(!pq.isEmpty()) {
            System.out.print(pq.peek()+" "); //peek in O(1)
            pq.remove(); //remove in O(logn)
        }
    }
}
