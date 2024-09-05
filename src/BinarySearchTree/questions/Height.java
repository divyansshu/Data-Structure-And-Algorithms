package BinarySearchTree.questions;

public class Height {
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

    public static int height(Node root) {

        if(root == null)
            return 0;

        int leftSubTree = height(root.left);
        int rightSubTree = height(root.right);

        //use the larger one
        if(leftSubTree > rightSubTree)
            return (leftSubTree + 1);
        else
            return (rightSubTree + 1);
    }
    public static void printGivenLevel(Node root, int level) {

        if(root == null) {
            return;
        }
        if(level == 1) {
            System.out.print(root.data+" ");
        }
        else { //level > 1
            printGivenLevel(root.left, level -1);
            printGivenLevel(root.right, level -1);
        }
    }
    public static void levelOrderBST(Node root) {

        if(root == null) {
            return;
        }
        int h = height(root);
        //print each level one by one
        for(int i = 1; i <= h; i++) {
            printGivenLevel(root, i);
            System.out.println();
        }
    }

    public static void main(String[] args) {

        int[] arr = {50,30,70,20,40,60,80};

        for(int i = 0; i < arr.length; i++) {
            root =  insert(root, arr[i]);
        }

        levelOrderBST(root);
        System.out.print("height of BST is : " +height(root));

    }
}
