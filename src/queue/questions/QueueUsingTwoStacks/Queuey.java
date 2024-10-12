package queue.questions.QueueUsingTwoStacks;

import java.util.Stack;

public class Queuey {

   static Stack<Integer> s1 = new Stack<>();
   static Stack<Integer> s2 = new Stack<>();

   //enqueue operation time Complexity: O(1)
    public static void enqueue(int x) {

        s1.push(x);
    }

    //dequeue time complexity: O(n)
    public static int dequeue() {
       while(!s1.isEmpty()) {
        s2.push(s1.pop());
       }
       int popped = s2.pop();

       while(!s2.isEmpty()) {
        s1.push(s2.pop());
       }
       return popped;
    }

    public static void display() {

        while(!s1.isEmpty()) {
            s2.push(s1.pop());
        }

        while(!s2.isEmpty()) {
            System.out.println(s2.peek());
            s1.push(s2.pop());
        }

    }

    public static void main(String[] args) {


        Queuey.enqueue(10);
        Queuey.enqueue(20);
        Queuey.enqueue(30);
        Queuey.enqueue(40);
        Queuey.enqueue(50);
        Queuey.display();
        System.out.println("popped element from Queue is: " +Queuey.dequeue());
        Queuey.display();

    }
}
