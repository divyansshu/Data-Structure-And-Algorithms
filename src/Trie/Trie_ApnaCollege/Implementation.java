package Trie.Trie_ApnaCollege;

public class Implementation {
    static class Node {
        Node[] children;
        boolean eow; //end of word

        public Node() {
            children = new Node[26];
            for(int i = 0; i < 26; i++) {
                children[i] = null;
            }
            this.eow = false;
        }
    }
    static Node root = new Node();

    public static void insert(String str) {
        Node currNode = root;
        int indx = 0;
        for(int i = 0; i < str.length(); i++) {
            indx = str.charAt(i) - 'a';

            if(currNode.children[indx] == null) {
                currNode.children[indx] = new Node();
            }
            if(i == str.length() - 1) {
                currNode.children[indx].eow = true;
            }

            currNode = currNode.children[indx];
        }
    }

    public static boolean search(String str) {

        int indx = 0;
        Node currNode = root;
        for(int i = 0; i < str.length(); i++) {
            indx = str.charAt(i) - 'a';
            Node node = currNode.children[indx];

            if(node == null)
                return false;

            if(i == str.length() - 1 && node.eow == false)
                return false;

            currNode = currNode.children[indx];
        }
        return true;
    }

    public static void main(String[] args) {
        String[] words = {"the", "a", "there", "their", "any"};
        for(int i = 0; i < words.length; i++) {
            insert(words[i]);
        }
        System.out.println(search("the"));
        System.out.println(search("they"));
    }

}
