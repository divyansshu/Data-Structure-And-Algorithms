package Linked_List.DoublyCircular;

public class Deletion {

    static Node head;
    static class Node {
        Node next;
        int data;
        Node prev;

        Node(int data) {
            this.data = data;
            this.next = null;
            this.prev = null;


        }
    }
    public void insert(int data) {
        Node newNode = new Node(data);
        if (head==null ) {

            newNode.next=newNode;
            newNode.prev=newNode;
            head=newNode;
            return;
        }
        Node temp = head;
        while (temp != null) {
            if (temp.next == head) {
                temp.next = newNode;
                newNode.prev = temp;
                newNode.next = head;
                head.prev = newNode;
                return;
            }
            temp = temp.next;

        }
    }

    public static void delHead() {
        Node temp=head;
        if(temp==null) {
            return;
        }
        if(temp.next==head){
            head=null;
            return;
        }
        if(temp.next != head){
            temp.next.prev=temp.prev;
            temp.prev.next=temp.next;
            head = temp.next;
            return;
        }
    }
    public void delend(){
        Node temp=head;
        if(temp==null) {
            return;
        }
        if(temp.next==head){
            head=null;
            return;
        }
        while (temp.next!=head){

            temp=temp.next;
        }
        if(temp.next==head){
            temp.prev.next=head;
            head.prev=temp.prev;
            return;
        }

    }
    public static void delmid(int pos){
        int count=2;
        if(pos==1){
            delHead();
            return;
        }
        Node temp=head;
        while(temp.next!=head){
            if(count==pos){
                temp.next.next.prev=temp;
                temp.next=temp.next.next;
                return;
            }
            temp=temp.next;
            count++;
        }
    }



    public  static  void printlist(){
        Node temp=head;
        while(temp.next!=head){
            System.out.print(temp.data +" ");
            temp=temp.next;

        }
        System.out.println(temp.data+" ");
    }

    public static void main(String[] args) {
        Deletion list = new Deletion();
        list.insert(11);
        list.insert(12);
        list.insert(13);
        list.insert(14);
        list.insert(15);
        list.insert(16);
        list.insert(17);
//            list.delHead();
            list.delend();
//        list.delmid(7);
        list.printlist();

    }

}
