package Linked_List.questions;

import java.lang.classfile.components.ClassPrinter.ListNode;
import java.util.ArrayList;
import java.util.Arrays;

public class SwappingNodes {

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

    /* this methods swap the nodes with the help of array
     * time complexity: O(n)
     * space complexity:O(n)
     */
    public void swapNodes(int k) {

        if (head == null)
            return;

        ArrayList<Integer> arr = new ArrayList<>();
        Node temp = head;

        // Copy data into array
        while (temp != null) {
            arr.add(temp.data);
            temp = temp.next;
        }

        int n = arr.size();
        int s = k - 1; // k-th node from the beginning (0-based index)
        int e = n - k; // k-th node from the end (0-based index)

        // Swap the elements
        int temp2 = arr.get(s);
        arr.set(s, arr.get(e));
        arr.set(e, temp2);

        // Reinsert sorted values into linked list
        temp = head;
        for (int num : arr) {
            temp.data = num;
            temp = temp.next;
        }
    }

        // Method to swap nodes without changing data
        /**
         * Swaps the k-th node from the beginning with the k-th node from the end in a linked list.
         *
         * Time Complexity: O(n), where n is the number of nodes in the linked list.
         * Space Complexity: O(1), as no extra space is used except for a few pointers.
         */
        public void swapNodes_2(int k) {
            Node temp1 = head;
            Node temp2 = head;
            Node prev1 = null;
            Node prev2 = null;

            // Find the k-th node from the beginning
            for (int i = 1; i < k; i++) {
                prev1 = temp1;
                temp1 = temp1.next;
            }

            Node temp = temp1;
            // Find the k-th node from the end
            while (temp.next != null) {
                prev2 = temp2;
                temp2 = temp2.next;
                temp = temp.next;
            }

            // Swap the nodes
            if (prev1 != null) {
                prev1.next = temp2;
            } else {
                head = temp2;
            }

            if (prev2 != null) {
                prev2.next = temp1;
            } else {
                head = temp1;
            }

            // Swap the next pointers
            Node tempNode = temp1.next;
            temp1.next = temp2.next;
            temp2.next = tempNode;
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

        SwappingNodes ll = new SwappingNodes();
        ll.insert(7);
        ll.insert(9);
        ll.insert(6);
        ll.insert(6);
        ll.insert(7);
        ll.insert(8);
        ll.insert(3);
        ll.insert(0);
        ll.insert(9);
        ll.insert(5);
        

        System.out.println("before swapping");
        ll.printlist();

        System.out.println("after swapping");
        // ll.swapNodes(5);
        ll.swapNodes_2(5);
        ll.printlist();
        
    }
    
}
