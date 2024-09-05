package BinarySearchTree.deletion;

import static java.nio.file.Files.delete;

public class BST {
    static Node root = null;
    static class Node {
        int data;
        Node left, right;

        public Node(int data) {
            this.data = data;
            this.left = right = null;
        }
    }
    public static Node insert(Node root, int val) {

        //case 1: if root is null
        if(root == null) {
            Node newNode = new Node(val);
            root = newNode;
            return root;
        }

        //case 2: if root is not null
        if(val < root.data) { //check if value is smaller than root then insert it in left subtree
            root.left = insert(root.left, val);
        }
        if(val > root.data){//check if value is greater than root then insert it in right subtree
            root.right = insert(root.right, val);
        }

        return root;
    }

    public static Node deleteNode(Node root, int key) {
        if(root == null) {
            return null;
        }
        if(root.data > key) {
            root.left = deleteNode(root.left, key);
        }
        else if(root.data < key) {
            root.right = deleteNode(root.right,key);
        }
        else {
            if(root.left == null && root.right == null)
                return null;

            else if(root.left == null)
                return root.right;

            else if (root.right == null) {
                return root.left;
            }
            else {
                Node temp = inorderSuccessor(root.right);
                root.data = temp.data;
                root.right = deleteNode(root.right, temp.data);
            }
        }
        return root;
    }

    public static Node inorderSuccessor(Node root) {
        while(root.left != null) {
            root = root.left;
        }
        return root;
    }

    public static void displayBST(Node root) {

        if(root == null) {
            return;
        }
        displayBST(root.left);
        System.out.print(root.data+" ");
        displayBST(root.right);
    }

    public static void main(String[] args) {

        int[] arr = {8,5,10,3,6,11,1,4,14};

        for(int i = 0; i < arr.length; i++) {
            root =  insert(root, arr[i]);
        }
        System.out.println("BST before deletion");
        displayBST(root);
        System.out.println("\nBST after deletion");

        root = deleteNode(root, 3);
        displayBST(root);



    }
}
