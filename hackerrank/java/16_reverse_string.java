// A palindrome is a word, phrase, number, or other sequence of characters 
// which reads the same backward or forward.
// Given a string `A`, print ` if it is a palindrome, print ` otherwise.

// Constraints
// `A` will consist at most `50` lower case english letters.

// Sample Input
// madam

// Sample Output
// Yes

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        boolean isPalindrome = true;
        int left = 0;
        int right = A.length()-1;
        while(left <= right){
            if (A.charAt(left) != A.charAt(right)){
                isPalindrome = false;
                break;
            }
            left++;
            right--;
        }
        if(isPalindrome){
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}


