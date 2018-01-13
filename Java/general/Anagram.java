import java.io.*;
import java.util.*;

public class Anagram {


  static boolean isAnagram(String inputA, String inputB) {
      // Remove all whitespace
      boolean status = true;
      String inputATrimed = inputA.trim().toLowerCase();
      String inputBTrimed = inputB.trim().toLowerCase();

      // Both two strings must be same length
      if (inputATrimed.length() != inputBTrimed.length()){
          status = false;
      }
      // convert into a char array
      char[] listOfCharsOfA = inputATrimed.toCharArray();
      // loop through the Chars and check if that specific char is presnet
      // in the target string
      for (char x : listOfCharsOfA){
          int index = inputBTrimed.indexOf(x);
          if(index != -1){
         // if so, remove that char from second string using Char.index
         // If character is present in inputBTrimed, removing that
         // char from inputBTrimed
              inputBTrimed = inputBTrimed.substring(0,index) +
               inputBTrimed.substring(index + 1, inputBTrimed.length());
          }else{
              status = false;
              break;
          }
       }
      return status;
  }

  public static void main(String[] args) {

    Scanner scan = new Scanner(System.in);
    String a = scan.next();
    String b = scan.next();
    scan.close();
    boolean ret = isAnagram(a, b);
    System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
  }
}
