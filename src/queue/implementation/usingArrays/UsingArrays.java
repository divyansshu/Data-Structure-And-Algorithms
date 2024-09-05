package queue.implementation.usingArrays;

public class UsingArrays {

    static class QueueY {
        static int front = -1;
        static int rear = -1;
        static int size;

        static int[] arr;

        QueueY(int size) {
            arr = new int[size];
            this.size = size;
        }

        //enqueue: insert an element at the end of the queue
        public  static void add(int data) {

            if(rear == size - 1) {
                System.out.println("queue is full");
                return;
            }

            arr[++rear] = data;
        }

        //dequeue: removes and returns an element from front of the queue
        public static int remove() {

            if(rear == -1){
                System.out.println("queue is empty");
                return -1;
            }

            front = arr[0];
            for(int i = 0; i < rear; i++) {
                arr[i] = arr[i+1];
            }
            rear--;
            return front;
        }

        //front: return an element from front without removing it
        public static int peek() {

            if(rear == -1) {
                System.out.println("queue is empty");
                return -1;
            }

            return arr[0];
        }

        public static boolean isEmpty(){
            return rear == -1;
        }
    }

    public static void main(String[] args) {

        QueueY q = new QueueY(5);
        q.add(10);
        q.add(20);
        q.add(30);
        q.add(40);
        q.add(50);


        while(!q.isEmpty()) {

            System.out.print(q.peek()+" ");
            q.remove();
        }

    }
}
