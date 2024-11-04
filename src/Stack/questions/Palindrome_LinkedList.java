package Stack.questions;

import java.util.Stack;

// Node class representing each node in the linked list
class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class Palindrome_LinkedList {

    private static Node head;

    // Method to insert a new node at the end of the list
    public static void insert(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }
        Node temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = newNode;
    }

    // Method to print the linked list
    public static void printList() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " -> ");
            temp = temp.next;
        }
        System.out.println("null");
    }

    // Method to reverse a linked list
    private static Node reverseList(Node head) {
        Node prev = null;
        Node current = head;
        Node nextNode = null;
        while (current != null) {
            nextNode = current.next;
            current.next = prev;
            prev = current;
            current = nextNode;
        }
        return prev;
    }


    /*
     * time complexity: O(n)
     * space complexity: O(n)
     */
//     public static boolean isPalindrome() {
//     Stack<Integer> s = new Stack<>();

//     Node temp = head;

//     while(temp!=null)
//     {
//         s.push(temp.data);
//         temp = temp.next;
//     }

//     boolean result = true;

//     temp=head;while(temp!=null)
//     {
//         if (temp.data == s.pop()) {
//             temp = temp.next;
//         } else {
//             result = false;
//             break;
//         }
//     }

//     return result;
// }

    /*
     * time complexity: O(n)
     * space complexity: O(1)
     */
    // Method to check if the linked list is a palindrome
    public static boolean isPalindrome() {
        if (head == null || head.next == null) {
            return true; // An empty list or a single node list is a palindrome
        }

        // Find the middle of the linked list using slow and fast pointers
        Node slow = head;
        Node fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Reverse the second half of the linked list
        Node secondHalf = reverseList(slow);
        boolean result = true;

        // Compare the first half and the reversed second half
        Node firstHalf = head;
        while (secondHalf != null) {
            if (firstHalf.data != secondHalf.data) {
                result = false;
                break;
            }
            firstHalf = firstHalf.next;
            secondHalf = secondHalf.next;
        }

        // Return the result of the comparison
        return result;
    }

    public static void main(String[] args) {
        // Palindrome_LinkedList list = new Palindrome_LinkedList();
        Palindrome_LinkedList.insert(1);
        Palindrome_LinkedList.insert(2);
        Palindrome_LinkedList.insert(3);
        Palindrome_LinkedList.insert(2);
        Palindrome_LinkedList.insert(1);

        Palindrome_LinkedList.printList(); // Output: 1 -> 2 -> 3 -> 2 -> 1 -> null

        System.out.println("Is palindrome: " + Palindrome_LinkedList.isPalindrome()); // Output: true
    }
}