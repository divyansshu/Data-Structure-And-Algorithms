package Linked_List.questions;

import java.util.*;

public class InsertionSortList {

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

    // Method to print the list
    public void printlist(Node head) {
        Node temp = head;
        if (temp == null)
            System.out.println("list is empty");

        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    // Method to sort the list using arrays
    /*
     * time complexity: O(nlogn)
     * space complexity: O(n)
     */
    public void sortList() {
        ArrayList<Integer> arr = new ArrayList<>();
        Node temp = head;

        // Copy data into array
        while (temp != null) {
            arr.add(temp.data);
            temp = temp.next;
        }

        // Sort the array
        Collections.sort(arr);

        // Reinsert sorted values into linked list
        temp = head;
        for (int num : arr) {
            temp.data = num;
            temp = temp.next;
        }
    }

    // Method to sort the list using insertion sort algorithm
    /*
     * time complexity: O(n^2)
     * space complexity: O(1)
     */
    public Node insertionSortList(Node head) {
        if (head == null || head.next == null) return head; // If list is empty or has one node

        Node dummy = new Node(0); // Dummy node to act as the new head of the sorted list
        dummy.next = head;
        Node prev = head;
        Node curr = head.next;

        while (curr != null) {
            if (curr.data >= prev.data) { // If current node is in the correct order
                prev = curr;
                curr = curr.next;
            } else {
                Node temp = dummy;
                // Find the correct position to insert the current node
                while (temp.next != null && curr.data > temp.next.data) {
                    temp = temp.next;
                }
                prev.next = curr.next; // Remove current node from its position
                curr.next = temp.next; // Insert current node in the correct position
                temp.next = curr;
                curr = prev.next; // Move to the next node
            }
        }
        return dummy.next; // Return the new head of the sorted list
    }

    public static void main(String[] args) {
        InsertionSortList ll = new InsertionSortList();

        ll.insert(4);
        ll.insert(2);
        ll.insert(1);
        ll.insert(3);   
        
        System.out.println("Original list:");
        ll.printlist(head);

        System.out.println("Sorted list:");
        Node sortedHead = ll.insertionSortList(head);
        ll.printlist(sortedHead);
    }
}
