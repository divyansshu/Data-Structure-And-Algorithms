package Linked_List.questions;

public class MiddleOf_linkedList {

    static class Node {
        int data;
        Node next;

        Node(int d) {
            data = d;
            next = null;
        }
    }
    static Node head = null;

    public void insert(int data) {
        Node newNode = new Node(data);
        Node temp = head;

        // if list is empty
        if (head == null) {
            head = newNode;
            return;
        }

        // if list contain more than one node
        while (temp.next != null) {

            temp = temp.next;
        }
        temp.next = newNode;
        newNode.next = null;
    }

    //return middle of linked list
    //using two pointers approach(optimized approach)
    public int middle() {
        Node slow = head;
        Node fast = head;

        while(fast != null && fast.next != null) {

            slow = slow.next;
            fast = fast.next.next;
        }
        return slow.data;
    }

    //brute force method
    public int middle_method2() {
        int count = 0;
        Node temp = head;

        while(temp != null) {
            temp = temp.next;
            count++;
        }

      temp = head;
      int mid = count/2;

      while(mid > 0) {
        temp = temp.next;
        mid--;
      }
      return temp.data;
    }

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
        MiddleOf_linkedList ll = new MiddleOf_linkedList();
        ll.insert(1);
        ll.insert(2);
        ll.insert(3);
        ll.insert(4);
        ll.insert(5);
        ll.insert(6);

        ll.printlist();

        System.out.println(ll.middle());
        System.out.println(ll.middle_method2());
        
    }
    
}
