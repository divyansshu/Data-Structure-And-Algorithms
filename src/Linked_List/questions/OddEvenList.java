package Linked_List.questions;

public class OddEvenList {

    static class Node {
        int data;
        Node next;

        Node(int d) {
            data = d;
            next = null;
        }
    }

    private static Node head;

    // Method to insert a new node at the end of the list
    public void insert(int data) {
        Node newNode = new Node(data);
        Node temp = head;

        // if list is empty
        if (head == null) {
            head = newNode;
            return;
        }

        // if list contains more than one node
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = newNode;
        newNode.next = null;
    }

    /*
     * time complexity: O(n)
     * space complexity: O(1)
     */
    public void oddEvenList() {

        if (head == null || head.next == null) {
            System.out.println("list only contains one node");
            return;
        }

        Node odd = head; // Start with the head as the first odd node
        Node even = head.next; // Start with the second node as the first even node
        Node evenHead = even; // Store the head of the even list

        // Traverse the list while there are more even and odd nodes
        while (even != null && even.next != null) {

            odd.next = even.next; // Link current odd node to the next odd node
            odd = odd.next; // Move odd pointer forward

            even.next = odd.next; // Link current even node to the next even node
            even = even.next; // Move even pointer forward

        }
        // Connect the end of the odd list to the head of the even list
        odd.next = evenHead;
    }

    // Method to print the list
    public void printlist() {
        Node temp = head;
        if (temp == null)
            System.out.println("list is empty");

        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        OddEvenList ll = new OddEvenList();
        ll.insert(1);
        ll.insert(2);
        ll.insert(3);
        ll.insert(4);
        ll.insert(5);

        System.out.println("list before arranging odd even indices together");
        ll.printlist();

        System.out.println("list after arranging odd even indices together");
        ll.oddEvenList();
        ll.printlist();
    }

}
