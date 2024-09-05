package Linked_List.questions.SumOfLastN_Nodes;

//program to calculate the sum of last n nodes

public class Last_N_nodesSum {

    Node head;
    static class Node {

        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
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

    public int sum(int N) {

//        Node temp = head;
        int count = 0;
        int sum = 0;
//
//        //getting count of nodes of linked list
//        while(temp != null) {
//        count++;
//        temp = temp.next;
//        }
//
//        while(count >= N) {
//
//            temp = head;
//
//            while(temp != null) {
//                if(count == N) {
//
//                    while(temp != null) {
//                        sum += temp.data;
//                        temp = temp.next;
//                    }
//                    break;
//                }
//                count--;
//                temp = temp.next;
//            }
//        }
//        return sum;



        if(head.next==null){
            return head.data;
        }
        Node temp=head;
        while(temp!=null){
            if(count>=N){
                if(temp.next==null){
                    break;
                }
                sum=sum+temp.data;
            }
            temp=temp.next;
            count++;
        }
        return sum;
    }



    public void printlist() {

        Node temp = head;

        if(temp == null)
            System.out.println("list is empty");

        while (temp != null) {
            System.out.print(temp.data + " -->");
            temp = temp.next;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {

        Last_N_nodesSum list = new Last_N_nodesSum();

        list.insert(10);
        list.insert(20);
        list.insert(30);
        list.insert(40);
        list.insert(50);

        list.printlist();

        System.out.println(list.sum(5));
    }
}
