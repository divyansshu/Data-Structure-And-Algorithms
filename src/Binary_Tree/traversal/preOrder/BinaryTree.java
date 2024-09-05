package Binary_Tree.traversal.preOrder;

import Binary_Tree.traversal.gfg_preorder.Traversal;

import java.util.ArrayList;

public class BinaryTree {

    static class Node {
        int data;
        Node left, right;

        Node(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }

    static class Preorder {

        static int index = -1;
        public static Node buildTree(ArrayList<Integer> nodes) {

            index++;
            if(nodes.get(index) == -1)
                return null;

            Node newNode = new Node(nodes.get(index)); //initializing the nodes
            newNode.left = buildTree(nodes);
            newNode.right = buildTree(nodes);

            return newNode;
        }
    }

    static ArrayList<Integer> tree = new ArrayList<Integer>();
    static ArrayList<Integer> preorder(Node root){


        if(root == null)
            return null;

        else {
            tree.add(root.data);
            preorder(root.left);
            preorder(root.right);
        }
        return tree;
    }

    public static void main(String[] args) {
       ArrayList<Integer> nodes = new ArrayList<>();

       nodes.add(2);
       nodes.add(2);
       nodes.add(7);
       nodes.add(5);
       nodes.add(-1);
       nodes.add(-1);
       nodes.add(2);
       nodes.add(-1);
       nodes.add(-1);
       nodes.add(10);
       nodes.add(-1);
       nodes.add(14);
       nodes.add(-1);
       nodes.add(-1);
       nodes.add(13);
       nodes.add(1);
       nodes.add(5);
       nodes.add(13);
       nodes.add(-1);
       nodes.add(-1);
       nodes.add(-1);
       nodes.add(11);
       nodes.add(-1);
       nodes.add(-1);
       nodes.add(10);
       nodes.add(5);
       nodes.add(-1);
       nodes.add(-1);
       nodes.add(5);
       nodes.add(-1);
       nodes.add(-1);

        Preorder tree = new Preorder();
        Node root = tree.buildTree(nodes);


//        for(int i = 0; i < nodes.size(); i++) {

            System.out.println(preorder(root));
//        }
    }
}
