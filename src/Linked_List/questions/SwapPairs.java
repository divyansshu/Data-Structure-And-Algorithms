package Linked_List.questions;

//swap nodes of a linked list in a pair of 2
public class SwapPairs {
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

    public void printlist() {

            Node temp = head;

        if(temp == null)
            System.out.println("list is empty");

        while (temp != null) {
            System.out.print(temp.data + " -->");
            temp = temp.next;
        }
    }
        public void swap() {

            Node temp = head;

            //case 1: if linked list is empty
            if(temp == null)
                return;

            //case 2: if list contain nodes
            while (temp != null && temp.next != null) {

                int val = temp.data;
                temp.data = temp.next.data;
                temp.next.data = val;
                temp = temp.next.next;
            }
        }

        public static void main(String[] args) {

            head = null;

            SwapPairs list = new SwapPairs();

//            list.insert(1);
//            list.insert(2);
//            list.insert(3);
//            list.insert(4);
//            list.insert(5);
//            list.insert(6);
            System.out.println("\nlinked list before swapping");
            list.printlist();
            list.swap();
            System.out.println("\nlinked list after swapping");
            list.printlist();
         }
    }

