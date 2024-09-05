package Binary_Tree.questions.subTree;

// program to check whether a tree is a subTree of another Tree
public class SubTree {

    static class Node {
        int data;
        Node left, right;

        public Node(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }



    static class BinaryTree {

        static int index = -1;
        public static Node buildTree(int[] nodes) {

            index++;
            if(nodes[index] == -1)
                return null;

            Node newNode = new Node(nodes[index]);
            newNode.left = buildTree(nodes);
            newNode.right = buildTree(nodes);

            return newNode;

        }
    }

    public static boolean isIdentical(Node root, Node subRoot) {

        if(root == null && subRoot == null)
            return true;

        if(root == null || subRoot == null)
            return false;

        if(root.data == subRoot.data)
        return isIdentical(root.left, subRoot.left) && isIdentical(root.right, subRoot.right);

        return false;
    }

    public static boolean isSubTree(Node root, Node subRoot) {

        //case 1: if root of main tree is null
        if(root == null)
            return false;

        //case 2: if root of subTree is equal to null;
        if(subRoot == null)
            return true;

        //case 3: if root of main tree is equal to root of subTree
        if(root.data == subRoot.data) {
            if(isIdentical(root, subRoot)) {
                return true;
            }
        }
        return isSubTree(root.left, subRoot) || isSubTree(root.right, subRoot);

        }

    public static void main(String[] args) {

        int[] mainTree = {1,2,4,-1,-1,5,-1,-1,3,-1,-1};

        int[] subTree = {2,4,-1,-1,5,-1,-1};

        BinaryTree tree = new BinaryTree();
        Node mainRoot = tree.buildTree(mainTree);
        Node subRoot = tree.buildTree(subTree);

        System.out.println(isSubTree(mainRoot, subRoot));


    }
}
