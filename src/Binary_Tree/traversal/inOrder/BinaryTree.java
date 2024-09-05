package Binary_Tree.traversal.inOrder;

public class BinaryTree {

    static class Node {
        int data;
        Node left;
        Node right;

        Node(int data) {
            this.data = data;
            this.left = this.right = null;
        }
    }

    static class Inorder {

       static int index = -1;

       public static Node buildTree(int nodes[]) {

           index++;
           if(nodes[index] == -1)
               return null;

           Node newNode = new Node(nodes[index]); //initializing the nodes
           newNode.left = buildTree(nodes);
           newNode.right = buildTree(nodes);

           return newNode;
       }

    }

    public static void inOrder(Node root) {

      if(root == null)
          return;

      inOrder(root.left);
        System.out.print(root.data + " ");
        inOrder(root.right);
    }

    public static void main(String[] args) {
        int nodes[] = {1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1};

        Inorder tree = new Inorder();
        Node root = tree.buildTree(nodes);
        inOrder(root);

    }
}
