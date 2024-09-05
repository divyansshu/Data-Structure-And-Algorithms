package Binary_Tree.traversal.gfg_preorder;

import java.util.ArrayList;

public class Traversal {

    class Node{
     int data;
     Node left,right;
     Node(int d){
         data=d;
         left=right=null;
     }
 }

    static ArrayList<Integer> preorder(Node root)
    {

        ArrayList<Integer> tree = new ArrayList<Integer>();
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

        int nodes[] = {1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1};
        Traversal traversal = new Traversal();

        

    }

    }
