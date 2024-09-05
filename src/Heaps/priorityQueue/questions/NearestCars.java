package Heaps.priorityQueue.questions;

import java.util.PriorityQueue;

public class NearestCars {

    static class Points implements Comparable<Points> {
        int x;
        int y;

        int distanceSq;
        int idx;

        public Points(int x, int y, int distanceSq, int idx) {
            this.x = x;
            this.y = y;
            this.distanceSq = distanceSq;
            this.idx = idx;
        }

        @Override
        public int compareTo(Points p2) {
            return distanceSq - p2.distanceSq;
        }
    }

    public static void main(String[] args) {

        int pts[][] = {{3,3}, {5,-1},{-2,4}};
        int k = 2;

        PriorityQueue<Points> pq = new PriorityQueue<>();
        for(int i = 0; i < pts.length; i++) {
            int disSq = (int) Math.sqrt(pts[i][0] * pts[i][0] + pts[i][1] * pts[i][1]);
            pq.add(new Points(pts[i][0], pts[i][1], disSq, i));
        }

        for(int i = 0; i < k; i++) {
            System.out.println("C"+ pq.remove().idx);
        }
    }

}
