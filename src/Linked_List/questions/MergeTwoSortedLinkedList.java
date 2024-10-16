package Linked_List.questions;

public class MergeTwoSortedLinkedList {
    
     Node head;
    // static Node head2;
    // static Node head3;

    static class Node {
        int data;
        Node next;

        Node(int d) {
            data = d;
            next = null;
        }
    }


    public static void MergeTwoLists(MergeTwoSortedLinkedList first, MergeTwoSortedLinkedList second) {

        Node temp1  = first.head;
        Node temp2 = second.head;
        MergeTwoSortedLinkedList sortedList = new MergeTwoSortedLinkedList();

        while(temp1 != null && temp2 != null) {
            if(temp1.data <= temp2.data) {
                sortedList.insert(temp1.data);
                temp1 =  temp1.next;
            }
            else {
                sortedList.insert(temp2.data);
                temp2 = temp2.next;
            }
        }
        while(temp1 != null) {
            sortedList.insert(temp1.data);
            temp1 = temp1.next;
        }
         while (temp2 != null) {
            sortedList.insert(temp2.data);
            temp2 = temp2.next;
        }

        sortedList.printlist();

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

        MergeTwoSortedLinkedList list1 = new MergeTwoSortedLinkedList();
        list1.insert(1);
        list1.insert(2);
        list1.insert(4);

        MergeTwoSortedLinkedList list2 = new MergeTwoSortedLinkedList();
        list2.insert(1);
        list2.insert(3);
        list2.insert(4);

        list1.printlist();
        list2.printlist();


       MergeTwoSortedLinkedList.MergeTwoLists(list1, list2);
        
    }
    
}
