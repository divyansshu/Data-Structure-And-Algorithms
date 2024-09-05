package Heaps.priorityQueue.questions;

import java.util.PriorityQueue;

public class ConnectNRopes {

    public static int minCost(PriorityQueue<Integer> pq) {

        int sum;
        int minSum = 0;

        while (pq.size() > 1) {
            sum = 0;
            sum = pq.remove() + pq.remove();
            minSum += sum;
            pq.add(sum);
        }
        return minSum;
    }
    public static void main(String[] args) {

        int[] arr = {4,3,2,6,3};

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i: arr) {
            pq.add(i);
        }

        System.out.println("minimum cost ot connect N ropes is: "+ minCost(pq));
    }
}
