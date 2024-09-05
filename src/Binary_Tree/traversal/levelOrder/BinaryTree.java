package Binary_Tree.traversal.levelOrder;

import java.util.LinkedList;
import java.util.Queue;
import java.util.logging.Level;

public class BinaryTree {

    static class Node {
        int data;
        Node left, right;

        Node(int data) {
            this.data = data;
            this.left = this.right = null;
        }
    }

    static class LevelOrder {

         static int index = -1;

        public static Node buildTree(int nodes[]) {

            index++;
            if(nodes[index] == -1)
                return null;

            Node newNode = new Node(nodes[index]);
            newNode.left = buildTree(nodes);
            newNode.right = buildTree(nodes);

            return newNode;

        }
    }

    public static void levelOrder(Node root) {

        if(root == null) {
            return;
        }
        Queue<Node>q = new LinkedList<>();
        q.add(root);
        q.add(null);

        while(!q.isEmpty()) {
            Node currNode = q.remove();

            if(currNode == null) {
                System.out.println();

                if(q.isEmpty()) {
                    break;
                }
                else {
                    q.add(null);
                }
            }
            else {
                System.out.print(currNode.data + " ");

                if(currNode.left != null) {
                    q.add(currNode.left);
                }

                if(currNode.right != null) {
                    q.add(currNode.right);
                }
            }

        }

    }

    public static void main(String[] args) {

        int nodes[] = {1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1};
        LevelOrder tree = new LevelOrder();
        Node root = tree.buildTree(nodes);
        levelOrder(root);
    }
}
