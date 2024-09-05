package Heaps.priorityQueue.Implementation;

import java.util.PriorityQueue;

public class PQ_with_Objects {
    //Comparable class is an interface which is used to
    // compare objects of a class to arrange them in sorted order
    static class Student implements Comparable<Student>{ //overriding
        String name;
        int rank;

        public Student(String name, int rank) {
            this.name = name;
            this.rank = rank;
        }

        @Override
        public int compareTo(Student s2) {
            return this.rank - s2.rank;
        }
    }

    public static void main(String[] args) {
        PriorityQueue<Student> pq = new PriorityQueue<>();

        pq.add(new Student("divyanshu", 1));
        pq.add(new Student("mayank", 5));
        pq.add(new Student("kartikey", 8));
        pq.add(new Student("shivam", 2));

        while(!pq.isEmpty()) {
            System.out.println(pq.peek().name+"->" + pq.peek().rank);
            pq.remove();
        }
    }
}
