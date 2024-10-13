package Stack.questions;

import java.util.LinkedList;
import java.util.Queue;


//implementation using two Queues:

/*
public class ImplementUsingQueue {

 * 
 * private Queue<Integer> q1;
 * private Queue<Integer> q2;
 * private int topElement;
 * 
 * public ImplementUsingQueue() {
 * q1 = new LinkedList<>();
 * q2 = new LinkedList<>();
 * }
 * 
 * public void push(int data) {
 * q1.add(data);
 * topElement = data;
 * }
 * 
 * public int pop() {
 * int popped = 0;
 * 
 * while (q1.size() > 1) {
 * topElement = q1.peek();
 * q2.add(q1.poll());
 * }
 * popped = q1.poll();
 * 
 * 
 * Queue<Integer> temp = q1;
 * q1 = q2; //assign all elements of q2 to q1
 * q2 = temp;//then make q2 again empty
 * 
 * return popped;
 * }
 * 
 * public int top() {
 * return topElement;
 * }
 * 
 * public boolean empty() {
 * return q1.isEmpty() && q2.isEmpty();
 * }
 */

 // implementation using single Queue:

public class ImplementUsingQueue {

    private Queue<Integer> q1;

    public ImplementUsingQueue() {
        q1 = new LinkedList<>();
    }

    public void push(int data) {
        q1.add(data);
        int size = q1.size();
        // Rotate the queue to move the newly added element to the front
        for (int i = 1; i < size; i++) {
            q1.add(q1.remove());
        }
    }

    public int pop() {
        if (q1.isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        return q1.remove();
    }

    public int top() {
        if (q1.isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        return q1.peek();
    }

    public boolean empty() {
        return q1.isEmpty();
    }

    public static void main(String[] args) {
        ImplementUsingQueue stack = new ImplementUsingQueue();
        stack.push(1);
        stack.push(2);
        System.out.println(stack.top()); // Output: 2
        System.out.println(stack.pop()); // Output: 2
        System.out.println(stack.top()); // Output: 1
        System.out.println(stack.pop()); // Output: 1
        System.out.println(stack.empty()); // Output: true
    }
}
