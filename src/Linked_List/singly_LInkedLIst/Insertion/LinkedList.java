package Linked_List.singly_LInkedLIst.Insertion;

public class LinkedList {
    static Node head;
    static class Node {
        int data;
        Node next;

        public Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    public static void insertHead(int data) {

        Node newNode = new Node(data);

        if(head == null) {
          head = newNode;
          head.next = null;
        }

        else {
            newNode.next = head;
            head = newNode;
        }

    }

    public static void deleteHead(int key) {

        Node temp = head;

        if(temp != null && key == temp.data) {
            head = temp.next;
            return;
        }
    }


    public static void printList(Node head) {

        Node temp = head;
        while(temp != null) {
            System.out.print(temp.data +" ");
            temp = temp.next;
        }
    }

    public static void main(String[] args) {

        LinkedList list = new LinkedList();
        list.insertHead(40);
        list.insertHead(30);
        list.insertHead(20);
        list.insertHead(10);

        list.deleteHead(10);

         printList(head);
    }
}
