package Binary_Tree.deletion;

import Binary_Tree.traversal.levelOrder.BinaryTree;

import java.util.LinkedList;
import java.util.Queue;

public class DeleteNode {

    static Node root = null;
    static class Node {
        int data;
        Node left, right;

        public Node(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }

    public static void printTree(Node root) {

        if(root == null) {
            return;
        }
        Queue<Node> q = new LinkedList<>();
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

    //function to delete deepest element in binary tree
    public static void deleteDeepestNode(Node root, Node deepestNode) {
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        Node temp = null;

        while(!q.isEmpty()) {
            temp = q.poll();

            if(temp == deepestNode) {
                temp = null;
                return;
            }

            if(temp.right != null) {
                if(temp.right == deepestNode) {
                    temp.right = null;
                    return;
                }
                else q.add(temp.right);
            }
            if(temp.left != null) {
                if(temp.left == deepestNode) {
                    temp.left = null;
                    return;
                }
                else q.add(temp.left);
            }
        }
    }

    public  static void deleteNode(Node root, int key) {

        //case 1: if tree is empty
        if(root == null) {
            System.out.println("no node is present in tree");
            return;
        }

        //case 2: if only root is present
        if(root.left == null && root.right == null) {
            if(root.data == key) {
                root = null;
                return;
            }
            else {
                return;
            }
        }

        //case 3: if tree contain nodes
        Node temp = null;
        Node keyNode = null;
        Queue<Node> q = new LinkedList<>();
        q.add(root);

        //do level order traversal until we find key and last node
        while(!q.isEmpty()) {
            temp = q.poll();

            if(temp.data == key)
                keyNode = temp;

            if(temp.left != null) {
                q.add(temp.left);
            }

            if(temp.right != null) {
                q.add(temp.right);
            }
        }
        if(keyNode != null) {
            keyNode.data = temp.data;
//            temp = null;
            deleteDeepestNode(root, temp);
            return;
        }

        else {
            System.out.println(key +" is not present in tree");
        }
    }

    public static void main(String[] args) {

        root = new Node(10);
        root.left = new Node(11);
        root.right = new Node(9);
        root.left.left = new Node(7);
//        root.left.left.left = new Node(8);
//        root.left.left.left.left = new Node(9);
        root.left.right = new Node(12);
        root.right.left = new Node(15);
        root.right.right = new Node(8);

        System.out.println("printing tree in level order before deletion");
        printTree(root);
        System.out.println();
        System.out.println("printing tree in level order after deletion");
        int key = 11;
        deleteNode(root, key);
        printTree(root);
    }


}
