package Linked_List.questions.reverse;

import Linked_List.questions.SwapPairs;

public class Reverse {
    static Node head;
    static class Node {
        int data;
        Node next;

        Node(int d) {
            data = d;
            next = null;
        }
    }

    public static void insert(int data) {

        Node newNode = new Node(data);
        Node temp = head;

        //if list is empty
        if (head == null) {
            head = newNode;
            return;
        }

        //if list contain more than one node
        while(temp.next != null) {

            temp = temp.next;
        }
        temp.next = newNode;
        newNode.next = null;
    }

    public static void printList(Node head) {

        Node temp = head;

        if(temp == null)
            System.out.println("list is empty");

        while (temp != null) {
            System.out.print(temp.data + " -->");
            temp = temp.next;
        }
    }
    public static void reverse() {

        Node temp = head;
        //if list is empty
        if(temp == null)
            return;

        //if not empty
        Node prev = null;
        Node nextNode = null;

        while(temp != null) {
            nextNode = temp.next;
            temp.next = prev;
            prev = temp;
            temp = nextNode;
        }

        printList(temp);
    }


    public static void main(String[] args) {

        head = null;

        Reverse list = new Reverse();
        list.insert(10);
        list.insert(20);
        list.insert(30);
        list.insert(40);
        list.insert(50);
        list.insert(60);
        System.out.println("list before reverse");
        list.printList(head);

        System.out.println("\nlist after reverse");

        list.reverse();
    }
}
