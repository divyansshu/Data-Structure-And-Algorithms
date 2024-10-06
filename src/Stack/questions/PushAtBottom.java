package Stack.questions;

//push at bottom of a stack
public class PushAtBottom {
    static Node root;
    static class Node{

        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    public boolean isEmpty() {
        if(root == null) {
            return true;
        }
        else
            return false;
    }

    public void push(int data) {

        Node newNode = new Node(data);

        if(root == null) {
            root = newNode;
        }
        else {
            Node temp = root;
            root = newNode;
            newNode.next = temp;
        }
    }

    //using loop
//    public static void swap() {
//
//        Node temp = root;
//        while(temp.next != null) {
//            int temp2 = temp.data;
//            temp.data = temp.next.data;
//            temp.next.data = temp2;
//
//            temp = temp.next;
//        }
//    }

    public int pop() {

        int popped = Integer.MIN_VALUE;

        if(root == null) {
            System.out.println("stack underflow");
            return -1;
        }
        else {
        popped = root.data;
        root = root.next;
        }
        return popped;

    }

    //using recursion
    public void pushAtBottom(int data, PushAtBottom list) {

        if(list.isEmpty()) {
            list.push(data);
            return;
        }
        int top = list.pop();
        pushAtBottom(data, list);
        list.push(top);
    }

    public void display() {
        if(root == null) {
            System.out.println("stack is empty");
        }
        else {
            Node temp = root;
            while(temp != null) {
                System.out.println(temp.data+" ");
                temp = temp.next;
            }
        }
    }

    public static void main(String[] args) {

        PushAtBottom list = new PushAtBottom();
        list.push(1);
        list.push(2);
        list.push(3);
        System.out.println("original stack");
        list.display();

//        list.swap();  using loop
        list.pushAtBottom(4, list); //using recursion
        System.out.println("stack after ");
        list.display();
    }
}
