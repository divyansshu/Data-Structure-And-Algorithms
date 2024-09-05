package BinarySearchTree.questions;

import java.lang.reflect.Array;
import java.util.ArrayList;

public class RoofToLeafPaths {
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

    public static void printPath(ArrayList<Integer> path) {
        for (int val: path) {
            System.out.print(val+" ");
        }
        System.out.println();
    }
    public static void printRoofToLeaf(Node root, ArrayList<Integer> paths) {

        if(root == null) {
            return;
        }
        paths.add(root.data);
        if(root.left == null && root.right == null) {
            printPath(paths);
        }else {
            printRoofToLeaf(root.left, paths);
            printRoofToLeaf(root.right, paths);
        }
        paths.remove(paths.size()-1);
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

        displayBST(root);
        System.out.println();
        ArrayList<Integer> paths = new ArrayList<>();
        printRoofToLeaf(root, paths);

    }
}
