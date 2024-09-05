package queue.questions.QueueUsingTwoStacks;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class Queuey {

    static Stack<Integer> s1 = new Stack<>();
   static Stack<Integer> s2 = new Stack<>();

    public static void enqueue(int x) {

        s1.push(x);
    }

    public static int dequeue() {

        if(s1.isEmpty() && s2.isEmpty()) {
            return -1;
        }

        if(s2.isEmpty()) {
            while(!s1.isEmpty()) {
                s2.push(s1.peek());
                s1.pop();
            }
        }

        int xx = s2.pop();
        return xx;
    }

    public static void main(String[] args) {

        Queuey q = new Queuey();
        q.enqueue(10);
        q.enqueue(20);
        q.enqueue(30);
        q.enqueue(40);
        q.enqueue(50);
        System.out.println(q.dequeue());

    }
}
