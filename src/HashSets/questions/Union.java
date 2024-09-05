package HashSets.questions;

import java.util.HashSet;

public class Union {

    public static int unionOfTwoArrays(int[] arr1, int[] arr2) {
        HashSet<Integer> set = new HashSet<>();
        for(int i = 0; i < arr1.length; i++) {
            set.add(arr1[i]);
        }

        for(int i = 0; i < arr2.length; i++) {
            set.add(arr2[i]);
        }

        return set.size();
    }
    public static void main(String[] args) {
        int[] arr1 = {7,3,9};
        int[] arr2 = {6,3,9,6,2,4};

        System.out.println(unionOfTwoArrays(arr1, arr2));
    }
}
