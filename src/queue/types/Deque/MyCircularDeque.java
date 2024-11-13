package queue.types.Deque;

public class MyCircularDeque {
    private int front = -1;
    private int rear = -1;
    private int size = 0;
    private int[] arr;
    private int capacity;

    MyCircularDeque(int n) {
        capacity = n;
        arr = new int[capacity];
    }

    public void insertLast(int value) {

        if (isFull()) {
            System.out.println("Queue is full");
            return;
        }

        if (isEmpty()) {
            front = rear = 0;
        }
        else rear = (rear + 1) % capacity;

        arr[rear] = value;
        size++;
        System.out.println("Inserted " + value + " at rear. Front: " + front + ", Rear: " + rear + ", Size: " + size);

    }

    public void insertFront(int value) {

        if (isFull()) {
            System.out.println("Queue is full");
            return;
        }

        if(isEmpty()) {
            front = rear = 0;
        }
        else {
            front = (front - 1 + capacity) % capacity;
        }
      
        arr[front] = value;
        size++;
        System.out.println("Inserted " + value + " at front. Front: " + front + ", Rear: " + rear + ", Size: " + size);

    }

    public void removeFront() {

        if (isEmpty()) {
            System.out.println("Queue is Empty");
            return;
        }

        int result = arr[front];
        if (front == rear)
            front = rear = -1;
        else
            front = (front + 1) % capacity;
        size--;
        System.out
                .println("Removed " + result + " from front. Front: " + front + ", Rear: " + rear + ", Size: " + size);
    }

    public void removeLast() {

        if (isEmpty()) {
            System.out.println("Queue is Empty");
            return;
        }

        int result = arr[rear];

        if(front == rear) {
            front = rear = -1;
        }
        else rear = (rear - 1 + capacity) % capacity;
        size--;
        System.out.println("Removed " + result + " from rear. Front: " + front + ", Rear: " + rear + ", Size: " + size);
        
    }

    public int getFront() {

        if (isEmpty()) {
            System.out.println("Queue is Empty");
            return -1;
        }

        return arr[front];

    }

    public int getLast() {
        if (isEmpty()) {
            System.out.println("Queue is Empty");
            return -1;
        }

        return arr[rear];
    }

    public boolean isFull() {
        return size == capacity;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public static void main(String[] args) {
        MyCircularDeque deque = new MyCircularDeque(5);
        deque.insertLast(1); // true
        deque.insertLast(2); // true
        deque.insertFront(3); // true
        deque.insertFront(4); // false, deque is full
        deque.removeLast(); // 2
        deque.insertFront(4); // true
        deque.removeFront(); // 4

    }

}
