package HashMaps.implementation;
import javax.sound.sampled.Line;
import java.util.*;
public class HashMapCode {
    static class HashMap<K, V> { //generics

        private class Node {
            K key;
            V value;

            public Node(K key, V value) {
                this.key = key;
                this.value = value;
            }
        }

        private int n; //number of nodes
        private int N; //number of buckets index
        private LinkedList<Node> buckets[]; //N = buckets.length

        @SuppressWarnings("unchecked")
        public HashMap() {
            this.N = 4;
            this.buckets = new LinkedList[4];
            for(int i = 0; i<N; i++) {
                this.buckets[i] = new LinkedList<>();
            }
        }

        private int hashFunction(K key) {
            int bi = key.hashCode();
            return Math.abs(bi) % N; //we want positive value only and in between 0 to N-1
        }

        private int searchInLL(K key, int bi) {
            LinkedList<Node> ll = buckets[bi];
            for(int i = 0; i < ll.size(); i++) {
                if(ll.get(i).key == key) {
                    return i; //dataIndex
                }
            }
            return -1; //key doesn't exists
        }

        private void rehash() {
            LinkedList<Node> oldBucket[] = buckets;
            buckets = new LinkedList[N*2];

            for(int i = 0; i < N*2; i++) {
                buckets[i] = new LinkedList<>();
            }

            for(int i = 0; i < oldBucket.length; i++) {
                LinkedList<Node> ll = oldBucket[i];
                for(int j = 0; j < ll.size(); j++) {
                    Node node = ll.get(j);
                    put(node.key, node.value);
                }
            }

        }

        public void put(K key, V value) {

            int bi = hashFunction(key); //bi = bucketIndex
            int di = searchInLL(key, bi); // di = dataIndex

            if(di == -1) { //key doesn't exist
                buckets[bi].add(new Node(key, value));
                n++; // increment the number of nodes
            }
            else { // key exists
                Node node = buckets[bi].get(di);
                node.value = value;
            }

            double lambda = (double) n/N;
            if(lambda > 2.0) { //2.0 is random constant value
                //hashing
            }

        }
        public boolean containsKey(K key) {

            int bi = hashFunction(key);
            int di = searchInLL(key, bi);

            if(di == -1) { //if key exists
                return false;
            }
            else { //if key doesn't exists
                Node node = buckets[bi].get(di);
                return true;
            }
        }

        public V remove(K key) {
            int bi = hashFunction(key);
            int di = searchInLL(key, bi);

            if(di == -1) { //if key exists
                return null;
            }
            else { //if key doesn't exists
                Node node = buckets[bi].remove(di);
                n--;
                return node.value;
            }
        }

        public V get(K key) {
            int bi = hashFunction(key);
            int di = searchInLL(key, bi);

            if(di == -1) { //if key exists
                return null;
            }
            else { //if key doesn't exists
                Node node = buckets[bi].get(di);
                return node.value;
            }
        }
        public ArrayList<K> keySet() {
            ArrayList<K> keys = new ArrayList<>();

            for(int i = 0; i < buckets.length; i++) {
                LinkedList<Node> ll = buckets[i];

                for(int j = 0; j < ll.size(); j++) {
                    Node node = ll.get(j);
                    keys.add(node.key);
                }
            }
            return keys;
        }

        public boolean isEmpty() {
            return n == 0;
        }
    }

    public static void main(String[] args) {

        HashMap<String, Integer> map = new HashMap<>();
        map.put("India", 140);
        map.put("USA", 180);
        map.put("UK", 150);

        ArrayList<String> keys = map.keySet();

        for(int i = 0; i < keys.size(); i++) {
            System.out.println(keys.get(i)+ " "+map.get(keys.get(i)));
        }
        System.out.println();

        System.out.println(map.isEmpty());

        System.out.println();
        map.remove("USA");
        System.out.println(map.get("USA"));
        map.remove("India");
        map.remove("UK");
        System.out.println(map.isEmpty());
//        for(int i = 0; i < keys.size(); i++) {
//            System.out.println(keys.get(i)+ " "+map.get(keys.get(i)));
//        }

    }
}
