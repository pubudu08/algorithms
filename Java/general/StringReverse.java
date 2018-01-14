import java.io.*;
import java.util.*;

public class StringReverse {

    public static String isPalindrome(String str) {
        return (str.equals(new StringBuilder(str).reverse().toString()))? "Yes": "No" ;
    }

    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        System.out.println(isPalindrome(A));
    }

}
