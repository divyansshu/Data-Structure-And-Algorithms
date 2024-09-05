package Binary_Tree.traversal.postOrder;

public class BinaryTree {

    static class Node {
        int data;
        Node left,right;

        Node(int data) {
            this.data = data;
            this.left = this.right = null;
        }
    }

    static class PostOrder {

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

    public static void postOrder(Node root) {

        if(root == null)
            return;

        postOrder(root.left);
        postOrder(root.right);
        System.out.print(root.data + " ");
    }

    public static void main(String[] args) {
        int nodes[] = {1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1};

        PostOrder tree = new PostOrder();
        Node root = tree.buildTree(nodes);
        postOrder(root);

    }
}
