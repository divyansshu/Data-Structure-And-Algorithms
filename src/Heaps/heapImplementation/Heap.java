package Heaps.heapImplementation;

import java.util.ArrayList;

public class Heap {
    static class HeapClass {
        ArrayList<Integer> arr = new ArrayList<>();

        public  void add(int data) { //O(log n)
            //add at last index
            arr.add(data);

            int x = arr.size() - 1; //x is child index
            int par = (x - 1) / 2; //parent index

            while (arr.get(x) < arr.get(par)) { //O(log n)

                //swap until min heap is maintained
                int temp = arr.get(x);
                arr.set(x, arr.get(par));
                arr.set(par, temp);

                x = par;
                par = (x - 1)/2;
            }
        }

        public int peek() {
        return arr.get(0);
        }

        private void heapify(int i) {
            int left = 2*i + 1;
            int right = 2*i + 2;
            int minIndx = i;

            if(left < arr.size() && arr.get(minIndx) > arr.get(left)) {
                minIndx = left;
            }

            if(right < arr.size() && arr.get(minIndx) > arr.get(right)) {
                minIndx = right;
            }

            if(minIndx != i) {
                //swap
                int temp = arr.get(i);
                arr.set(i, arr.get(minIndx));
                arr.set(minIndx, temp);

                heapify(minIndx);
            }
        }

        public int remove() {
            int data = arr.get(0);
            // to remove root element
            //step 1: swap first and last
            int temp = arr.get(0);
            arr.set(0, arr.get(arr.size() - 1));
            arr.set(arr.size() - 1, temp);

            //step 2 : delete last
            arr.remove(arr.size() - 1);

            //step 3: heapify function call to maintain heap
            heapify(0);
            return data;
        }

        public boolean isEmpty() {
            return arr.size() == 0;
        }
    }

    public static void main(String[] args) {

        HeapClass h = new HeapClass();
        h.add(1);
        h.add(2);
        h.add(4);
        h.add(6);
        h.add(5);
        h.add(3);
        h.add(9);
        h.add(8);

        while(!h.isEmpty()) { //heap sort - O(nlogn)
            System.out.print(h.peek()+" ");
            h.remove();
        }

    }
    }
