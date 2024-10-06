package Stack.Implementation.UsingLInkedList;

public class StackAsLInkedList {

    StackNode top;
    static class StackNode {
        int data;
        StackNode next;

        StackNode(int data) {
            this.data = data;
            this.next = null;
        }
    }

    public boolean isEmpty() {
        if(top == null) {
            return true;
        }
        else
            return false;
    }

    public void push(int data) {
        StackNode newNode = new StackNode(data);

        if(top == null) {
            top = newNode;
        }
        else {
            StackNode temp = top;
            top = newNode;
            newNode.next = temp;
        }
        System.out.println(data + " pushed to stack");
    }

    public int pop() {
        int popped = Integer.MIN_VALUE;
        if(top == null) {
            System.out.println("stack is empty");
        }
        else {
            popped = top.data;
            top = top.next;
        }
        return popped;
    }

    public int peek() {

        if(top == null) {
            System.out.println("stack is empty");
            return Integer.MIN_VALUE;
        }
        else {
            return top.data;
        }
    }

    public void print() {

        if(top == null) {
            System.out.println("stack is empty");
        }
        StackNode temp = top;
        while(temp != null) {
            System.out.print(temp.data+" ");
            temp = temp.next;
        }
    }

    public static void main(String[] args) {

        StackAsLInkedList s = new StackAsLInkedList();
        s.push(10);
        s.push(20);
        s.push(30);

        s.print();
        System.out.println();
        System.out.println(s.pop() + " popped from stack");
        System.out.println("top element is "+ s.peek());
        s.print();
    }

}
