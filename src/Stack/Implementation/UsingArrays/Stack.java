package Stack.Implementation.UsingArrays;

public class Stack {

    static final int MAX = 1000;
    int top;
    int a[] = new int[MAX]; //maximum size of stack

    boolean isEmpty() {
        return (top < 0);
    }
    Stack() {
        top = -1;
    }

    boolean push(int x) {
        if(top >= (MAX -1)) {
            System.out.println("stack overflow");
        return false;
        }
        else {
            a[++top] = x;
            System.out.println(x + " pushed into stack");
            return true;
        }
    }

    int pop() {
        if(top < 0) {
            System.out.println("stack underflow");
            return 0;
        }
        else {
            int x = a[top--];
            return x;
        }
    }

    int peek() {
        if(top < 0) {
            System.out.println("stack underflow");
            return 0;
        }
        else {
            int x = a[top];
            return x;
        }
    }

    void print() {
        for(int i = top; i > -1; i--) {
            System.out.println(" "+ a[i]);
        }
    }
}

class Main {
    public static void main(String[] args) {

        Stack s = new Stack();
        s.push(10);
        s.push(20);
        s.push(30);
        s.print();
        System.out.println(s.pop() + "popped from stack");
        System.out.println("top element is : "+ s.peek());
        System.out.println("Elements present in stack: ");
        s.print();
    }
}
