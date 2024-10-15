package Linked_List.questions;

public class RemoveDuplicate_fromLinkedList {

    static Node head;

    static class Node {
        int data;
        Node next;

        Node(int d) {
            data = d;
            next = null;
        }
    }

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


//function to remove duplicates from sorted linked list
      public void deleteDuplicates() {

        if(head == null) {
            System.out.println("list is empty");
            return;
        }

       Node curr = head;
       while(curr.next != null) {
        if(curr.data == curr.next.data) {
            curr.next = curr.next.next;
        }
        else {
            curr = curr.next;
        }
       }
       printlist();
       
    }

    public void printlist() {

        Node temp = head;

        if (temp == null)
            System.out.println("list is empty");

        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
    }

    public static void main(String[] args) {
        RemoveDuplicate_fromLinkedList list = new RemoveDuplicate_fromLinkedList();
        list.insert(1);
        list.insert(1);
        list.insert(2);
        list.insert(3);
        list.insert(3);
//        list.printlist();
        list.deleteDuplicates();
    }

}