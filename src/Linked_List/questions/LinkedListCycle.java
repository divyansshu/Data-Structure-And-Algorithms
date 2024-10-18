package Linked_List.questions;

import java.lang.classfile.components.ClassPrinter.ListNode;

public class LinkedListCycle {
    static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

private static Node head = null;

// Method to insert a new node at the end of the list
public static void insert(int data) {
    Node newNode = new Node(data);

    if (head == null) {
        head = newNode;
        return;
    } else {
        Node temp = head;

        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = newNode;
    }
}

// Method to create a cycle in the linked list
public static void createCycle(int pos) {
    if (head == null)
        return;

    Node temp = head;
    Node cycleNode = null;
    int count = 0;

    while (temp.next != null) {
        if (count == pos) {
            cycleNode = temp;
        }
        temp = temp.next;
        count++;
    }
    // Create a cycle by pointing the last node to the cycleNode
    temp.next = cycleNode;
}

// Method to detect a cycle in the linked list
public static boolean hasCycle() {

        Node fast = head;
        Node slow = head;

        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next;

            if(fast == slow) return true;
        }
        return false;
      }

    public static void display() {
        if (head == null) {
            System.out.println("list is empty");
            return;
        }
        else {
            Node temp = head;

            while (temp != null) {
                System.out.print(temp.data +" ");
                temp = temp.next;
            }
        
        }
    }

    public static void main(String[] args) {
        
        insert(1);
        insert(2);
        insert(3);
        insert(4);
        insert(5);

        // Creating a cycle for testing
        createCycle(2); // Creates a cycle at node with value 3

        // display();
        System.out.println(hasCycle());

        // Breaking the cycle for testing display
        head.next.next.next.next.next = null;
        display();

    }
    
}
