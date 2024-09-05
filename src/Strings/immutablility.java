package Strings;

class immutability {

public static void main(String[] args) {

    String name = "divyanshu";
    String lname = "divyanshu";

    if(name == lname) {
        System.out.println(true);
    } else
        System.out.println(false);


    System.out.println(lname);
    System.out.println(name);
    
}

}