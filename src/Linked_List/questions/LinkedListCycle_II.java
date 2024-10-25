package Linked_List.questions;

public class LinkedListCycle_II {

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

    //method to return the length of cycle in a linked list
    public static int lengthCycle(Node slow) {
        Node temp = slow;
        int length = 0;
        do {
            temp = temp.next;
            length++;
        }while(slow != temp);
        return length;
    }

    //method to check if a linked list has a cycle or not
    public static Node hasCycle() {
       int length = 0;

       Node fast = head;
       Node slow = head;

       while(fast != null && fast.next != null) {
        fast = fast.next.next;
        slow  = slow.next;

        if(slow == fast) {
            length = lengthCycle(slow);
            break;
        }

       }

       if(length == 0) return null;

       fast = head;
       slow = head;

       while(length > 0) {
        slow = slow.next;
        length--;
       }

       while(slow != fast) {
        fast = fast.next;
        slow = slow.next;
       }
       return slow;
    }

    public static void display() {
        if (head == null) {
            System.out.println("list is empty");
            return;
        } else {
            Node temp = head;

            while (temp != null) {
                System.out.print(temp.data + " ");
                temp = temp.next;
            }

        }
    }

    public static void main(String[] args) {
        insert(3);
        insert(2);
        insert(0);
        insert(-4);

        // Creating a cycle for testing
        createCycle(2); // Creates a cycle at node with value 3

        // display();
        System.out.println(hasCycle());

        // Breaking the cycle for testing display
        // head.next.next.next.next.next = null;
        // display();
    }
    
}
