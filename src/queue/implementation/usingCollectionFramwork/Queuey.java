package queue.implementation.usingCollectionFramwork;

import java.util.*;
public class Queuey {

    public static void main(String[] args) {

        Queue<Integer> q = new LinkedList<>();
        q.add(10);
        q.add(20);
        q.add(30);
        q.add(40);
        q.add(50);
        q.add(60);

        while(!q.isEmpty()) {
            System.out.println(q.peek()+" ");
            q.remove();
        }

    }
}
