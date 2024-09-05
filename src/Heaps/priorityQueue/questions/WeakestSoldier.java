package Heaps.priorityQueue.questions;

import java.util.PriorityQueue;

public class WeakestSoldier {

    static class Soldier implements Comparable<Soldier>{

        int indx;
        int countOfSoldier;

        public Soldier(int indx, int countOfSoldier) {
            this.indx = indx;
            this.countOfSoldier = countOfSoldier;
        }

        @Override
        public int compareTo(Soldier s2) {
            if(this.countOfSoldier == s2.countOfSoldier) {
                return this.indx - s2.indx;
            }
            else {
                return this.countOfSoldier - s2.countOfSoldier;
            }
        }
    }

    public static void main(String[] args) {

        int[][] matrix = {{1,0,0,0}, //1 denotes soldier and 0 denotes civilian
                          {1,1,1,1},
                          {1,0,0,0},
                          {1,0,0,0}};
        int k = 2;

        PriorityQueue<Soldier> pq = new PriorityQueue<>();
        for(int i = 0; i< matrix.length; i++) {
            int count = 0;
            for(int j = 0; j < matrix[i].length; j++) {
                 count += matrix[i][j] == 1 ? 1 : 0;
            }
            pq.add(new Soldier(i, count));
        }

        for(int i = 0; i < k; i++) {
            System.out.println("Rows with minimum soldier is R"+pq.remove().indx);
        }
    }
}
