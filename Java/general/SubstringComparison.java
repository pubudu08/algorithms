import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class SubstringComparison {

    public static String getSmallestAndLargest(String input, int length) {
        String smallest = "";
        String largest = "";

        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'

        for (int x = 0; x <= input.length() - length ; x++){
            String subString = input.substring(x , x + length);

            if(x == 0){
                smallest = subString;
            }

            if(subString.compareTo(largest)>0){
                largest = subString;
            }else if(subString.compareTo(smallest)<0)
                smallest = subString;
        }
        return smallest + "\n" + largest;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();

        System.out.println(getSmallestAndLargest(s, k));
    }
}
