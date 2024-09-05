package Binary_Tree.questions.countNodes;

public class CountOfNodes {

    static class Node{
        int data;
        Node left, right;

        Node(int data) {
            this.data = data;
             this.left = this.right = null;
        }
    }

    static class BinaryTree {

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

    public static int countNumOfNodes(Node root) {

        if(root == null)
            return 0;

        int leftNodes = countNumOfNodes(root.left);
        int rightNodes = countNumOfNodes(root.right);

        return leftNodes + rightNodes +1;
    }

    public static void main(String[] args) {

        int nodes[] = {1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1};

        BinaryTree tree = new BinaryTree();
        Node root = tree.buildTree(nodes);
        System.out.println(countNumOfNodes(root));
    }
}
