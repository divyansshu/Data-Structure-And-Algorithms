package Stack.Implementation.UsingArrayList;

import java.util.ArrayList;

public class StackAsArrayList {

    static ArrayList<Integer> list = new ArrayList<>();
    public static boolean isEmpty() {
        return list.size() == 0;
    }

    public static void push(int data) {
        list.add(data);
    }

    public static int pop() {

        if(isEmpty())
            return -1;

        int top = list.get(list.size()-1);
        list.remove(list.size()-1);
        return top;
    }

    public static int peek() {
        if(isEmpty())
            return -1;

        return list.get(list.size()-1);
    }

    public static void main(String[] args) {
        StackAsArrayList s = new StackAsArrayList();
        s.push(20);
        s.push(30);
        s.push(40);
        s.push(50);

        while(!s.isEmpty()){
            System.out.println(s.peek());
            s.pop();
        }
    }


}