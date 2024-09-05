package Binary_Tree.questions.heightTree;


public class HeightOfTree {

    static class Node {
        int data;
        Node left, right;

        public Node(int data) {
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

    public static int heightOfTree(Node root) {

        if(root == null)
            return 0;

        int leftNodeHeight = heightOfTree(root.left);
        int rightNodeHeight = heightOfTree(root.right);

        int maxHeight = Math.max(leftNodeHeight, rightNodeHeight) + 1;

        return maxHeight;
    }

    public static void main(String[] args) {

        int[] nodes = {1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1};

        BinaryTree tree = new BinaryTree();
        Node root = tree.buildTree(nodes);
        System.out.println(heightOfTree(root));

    }
}
