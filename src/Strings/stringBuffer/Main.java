// The code snippet creates StringBuffer objects using different constructors,
// determines the capacity of the string,
// appends a string to the buffer,
// and generates a random string of length 10.

package Strings.stringBuffer;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {

        //default constructor
        StringBuffer buffer = new StringBuffer();
        System.out.println(buffer.capacity());
        buffer.append("Hello World");
        System.out.println(buffer);

        //parameterized constructor
         StringBuffer buffer2 = new StringBuffer("Divyanshu Rawat");
        System.out.println(buffer2.toString());

        //determine the capacity of string
        StringBuffer buffer3 = new StringBuffer(10);
        System.out.println(buffer3.capacity());
        buffer3.append("gauravrawat");
        System.out.println(buffer3.capacity());
        System.out.println(buffer3.toString());

//generating random characters and appending them to a single string object
        int n = 10;
        String str = RandomString.generate(n);
        System.out.println(str);

        String names = "gaurav Mayank shivam kartikey aryan aman";
        String[] arr = names.split(" ");
        System.out.println(Arrays.toString(arr));


    }
}
