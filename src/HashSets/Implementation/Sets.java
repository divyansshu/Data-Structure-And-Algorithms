package HashSets.Implementation;

import java.util.HashSet;
import java.util.Iterator;

public class Sets {

    public static void main(String[] args) {

        HashSet<Integer> set = new HashSet<>();
        set.add(1);
        set.add(2);
        set.add(3);
        set.add(4);
        set.add(5);
        set.add(5);//set does not add duplicate elements

        System.out.println(set.remove(4));
        System.out.println(set.contains(3));

        Iterator it = set.iterator();

        while(it.hasNext()) {
            System.out.print(it.next()+" ");
        }

    }
}
