//package Trie.questions;
//
//public class WordBreakProblem {
//    static class Node {
//        Node[] children;
//        boolean eow;
//
//        public Node() {
//            children = new Node[26];
//            for(int i = 0; i < 26; i++) {
//                children[i] = null;
//            }
//            this.eow = false;
//        }
//    }
//    static Node root = new Node();
//
//    public static void insert(String str) {
//        Node currNode = root;
//        int indx = 0;
//        for (int i = 0; i < str.length(); i++) {
//            indx = str.charAt(i) - 'a';
//
//            if(currNode.children[indx] == null) {
//                currNode.children[indx] = new Node();
//            }
//            if(i == str.length() - 1) {
//                currNode.children[indx].eow = true;
//            }
//            currNode = currNode.children[indx];
//        }
//    }
//
//    public static boolean search(String str) {
//        Node currNode = root;
//        int indx = 0;
//        String string = "";
//        for (int i = 0; i< str.length(); i++) {
//            indx = str.charAt(i) - 'a';
//            Node node = currNode.children[indx];
//
//            if(node == null)
//                return false;
//
//            if(i == )
//
//
//
//
//        }
//    }
//    public static void main(String[] args) {
//        String[] words = {"i", "like", "sam", "samsung", "mobile", "ice"};
//        String myString = "ilikesamsung";
//
//        for(int i = 0; i< words.length; i++) {
//
//            insert(words[i]);
//        }
//
//        System.out.println(search(myString));
//    }
//}
