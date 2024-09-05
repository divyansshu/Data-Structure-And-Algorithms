package Binary_Tree.questions.sumNodes_KthLevel;

import java.util.LinkedList;
import java.util.Queue;

public class KthLevelSum {

    static class Node {
        int data;
        Node left, right;

         Node(int data) {
            this.data = data;
            this.left = this.right = null;
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

 // Function to return the sum of all
// the nodes at Kth level using
// level order traversal
    public static int sumKLevel(Node root, int k) {

        //if the root node is null
        if(root == null)
            return 0;



        //create the queue
        Queue<Node> q = new LinkedList<>();

        //enqueue the root node
        q.add(root);

        //level is used to track the  current level
        int level = 1;

        //to store the sum of nodes at kth level
        int sum = 0;

        // flag is used to break out of
        // the loop after the sum of all
        // the nodes at Nth level is found
        int flag = 0;

        // Iterate the queue till it's not empty
        while(!q.isEmpty()) {

            // Calculate the number of nodes
            // in the current level
            int size = q.size();

            // Process each node of the current
            // level and enqueue their left
            // and right child to the queue
            while(size-- > 0) {

                Node currNode = q.peek();
                q.remove();


                // If the current level matches the
                // required level then calculate the
                // sum of all the nodes at that level
                if(level == k) {

                    // Flag initialized to 1
                    // indicates that sum of the
                    // required level is calculated
                    flag = 1;

                    // Calculating the sum of the nodes
                    sum += currNode.data;
                }
                else {

                    // Traverse to the left child
                    if(currNode.left != null) {
                        q.add(currNode.left);
                    }
                    // Traverse to the right child
                    if(currNode.right != null) {
                        q.add(currNode.right);
                    }
                }
            }

            // Increment the variable level
            // by 1 for each level
            level++;

            // Break out from the loop after the sum
            // of nodes at K level is found
            if(flag == 1)
                break;
            }
        return sum;
        }

    public static void main(String[] args) {

        int[] nodes = {1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1};
        BinaryTree tree = new BinaryTree();
        Node root = tree.buildTree(nodes);

        int k = 4;
        System.out.println(sumKLevel(root, k));
    }


}
