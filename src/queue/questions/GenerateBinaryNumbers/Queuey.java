package queue.questions.GenerateBinaryNumbers;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Queuey {

    //Function to generate binary numbers from 1 to N using a queue.
    static ArrayList<String> generate(int N) {

        ArrayList<String> binary = new ArrayList<>();

        Queue<String> q = new LinkedList<>();

        q.add("1");

        while(N-- > 0) {

            String s1 = q.peek();
            q.remove();

            binary.add(s1);

            String s2 = s1;

            q.add(s1 + "0");
            q.add(s2 + "1");
        }

        return binary;
        // Your code here
    }

    public static void main(String[] args) {

        Queuey qq = new Queuey();

        System.out.println(generate(5));

//        int num = 10; // number of binary numbers to generate
//
//        Queue<String> queue = new LinkedList<>();
//        queue.add("1");
//
//        for (int i = 0; i < num; i++) {
//            String s1 = queue.peek();
//            queue.add(s1 + "0");
//            queue.add(s1 + "1");
//            System.out.println(queue.poll());
//        }

    }
}
