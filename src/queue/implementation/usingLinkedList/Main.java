package queue.implementation.usingLinkedList;

public class Main {
    public static void main(String[] args) {

        QueueY q = new QueueY();
        q.add(10);
        q.add(20);
        q.add(30);
        q.add(40);
        q.add(50);

        System.out.println();
        System.out.println(q.remove());
        System.out.println();
        System.out.println(q.peek());
        System.out.println();
        q.display();

    }
}
