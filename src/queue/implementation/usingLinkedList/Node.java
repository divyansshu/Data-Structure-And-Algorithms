package queue.implementation.usingLinkedList;//package queue.implementation;

    public class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    class QueueY {
        Node front, rear;

        QueueY() {
            this.rear = this.front = null;
        }

        //enqueue
        public void add(int data) {
            Node newNode = new Node(data);

            if (this.rear == null) {
                this.rear = this.front = newNode;
                return;
            }

            this.rear.next = newNode;
            this.rear = newNode;
        }

        //dequeue
        public int remove() {

            if (this.front == null) {
                System.out.println("queue is empty");
                return -1;
            }
            Node temp = this.front;
            this.front = this.front.next;

            if (this.front == null) {
                this.rear = null;
            }
            return temp.data;
        }

        public int peek() {

            if (this.front == null) {
                System.out.println("queue is empty");
                return -1;
            }

            return front.data;
        }

        public void display() {
            Node temp = front;
            while (front != null) {
                System.out.print(front.data + " ");
                front = front.next;
            }
        }
    }

