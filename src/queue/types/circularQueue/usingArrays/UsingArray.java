package queue.types.circularQueue.usingArrays;

public class UsingArray {

    static class CircularQueue {

         static int rear = -1;
        static int front = -1;
        static int size;
        static int[] arr;

        CircularQueue(int size) {
            arr = new int[size];
            this.size = size;
        }

        public static boolean isEmpty() {
             return rear == -1 && front == -1;
        }
        public static boolean isFull() {
            return front == (rear+1) % size;
        }

        public static void add(int data) {
            if(isFull()) {
                System.out.println("queue is full");
                return;
            }

            //when first element is inserted
            if(front == -1) {
                front = 0;
            }
            rear = (rear+1) % size;
            arr[rear] = data;
        }

        public static int remove() {
            if(isEmpty()) {
                System.out.println("queue is empty");
                return -1;
            }

            int result = arr[front];
            if(front == rear) {
                front = rear = -1;
            }
            else {
                front = (front+1) % size;
            }

            return result;
        }

        public static int peek() {

            if(isEmpty()) {
                System.out.println("queue is empty");
                return -1;
            }

            return arr[front];
        }
    }

    public static void main(String[] args) {

        CircularQueue q = new CircularQueue(6);

        q.add(10);
        q.add(20);
        q.add(30);
        q.add(40);
        q.add(50);
        q.add(60);

        System.out.println(q.remove()+" is removed from front");

        q.add(70);

        System.out.println(q.peek()+" is in the front");

        while(!q.isEmpty()) {
            System.out.print(q.peek()+" ");
            q.remove();
        }

    }
}
