package BinarySearchTree.questions;

public class TotalNodes {
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
        if(root == null) {Node newNode = new Node(val);
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

    public static int numberOfNodes(Node root) {
        if(root == null)
            return 0;

        int total_LeftSubTree = numberOfNodes(root.left);
        int total_rightSubTree = numberOfNodes(root.right);

        return total_LeftSubTree + total_rightSubTree + 1;
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

        int[] arr = {50,30,70,20,40,60,80};

        for(int i = 0; i < arr.length; i++) {
            root =  insert(root, arr[i]);
        }

//        displayBST(root);
        System.out.println(numberOfNodes(root));

    }
}
