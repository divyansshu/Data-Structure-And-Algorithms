package Binary_Tree.insertion.levelOrder;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class BinaryTree {

    static class Node {

        int data;
        Node left, right;

        Node(int data) {
            this.data = data;
            this.left = this.right = null;
        }
    }

    static class Insertion {

        static int index = -1;

        public static Node buildTree(ArrayList<Integer> nodes) {

            index++;
            if (nodes.get(index) == -1) {
                return null;
            }

            Node newNode = new Node(nodes.get(index));
            newNode.left = buildTree(nodes);
            newNode.right = buildTree(nodes);
            return newNode;

        }
    }

    public static void printTree(Node root) {
        // printing tree in level order
        if (root == null) {
            System.out.println("no nodes are present in tree");
            return;
        }

        Queue<Node> q = new LinkedList<>();
        q.add(root);
        q.add(null);

        while (!q.isEmpty()) {

            Node currNode = q.peek();
            q.remove();

            if (currNode == null) {
                System.out.println();

                if (q.isEmpty())
                    break;

                else
                    q.add(null);
            } else {
                System.out.print(currNode.data + " ");

                if (currNode.left != null) {
                    q.add(currNode.left);
                }

                if (currNode.right != null) {
                    q.add(currNode.right);
                }
            }
        }

    }

    public static void main(String[] args) {

        // int nodes[] = {1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1};
        ArrayList<Integer> nodes = new ArrayList<>();
        nodes.add(10);
        nodes.add(20);
        nodes.add(40);
        nodes.add(-1);
        nodes.add(-1);
        nodes.add(50);
        nodes.add(-1);
        nodes.add(-1);
        nodes.add(30);
        nodes.add(-1);
        nodes.add(60);
        nodes.add(-1);
        nodes.add(-1);

        Insertion tree = new Insertion();
        Node root = tree.buildTree(nodes);
        printTree(root);

        System.out.println(nodes);
    }
}
