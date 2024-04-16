// We use the integers , , and  to create the following series:

// (a + 2^0 • b), (a + 2^0 • b + 2^1 • b), ..., (a + 2^0 • b + 2^1 • b +...+2^n-1 • b）

// You are given `q` queries in the form of `a`, `b`, and `n`. For each query, 
// print the series corresponding to the given `a`, `b`, and `n` values as a 
// single line of `n` space-separated integers.

// Input Format
// The first line contains an integer, `q`, denoting the number of queries.
// Each line `i` of the `q` subsequent lines contains three space-separated 
// integers describing the respective `a_i`, `b_i`, and `n_i` values for that query.

// Output Format
// For each query, print the corresponding series on a new line. Each series must 
// be printed in order as a single line of  space-separated integers.

// Sample Input
// 2
// 0 2 10
// 5 3 5

// Sample Output
// 2 6 14 30 62 126 254 510 1022 2046
// 8 14 26 50 98

// Explanation
// We have two queries:
// 1. We use a = 0, b = 2, and n = 10 to produce some series so, 8_0, 8_1, ..., 8_n-1:
// 8_0 = 0 + 1 • 2 = 2
// 8_1 = 0 + 1 • 2 + 2 • 2 = 6
// 8_2 = 0 + 1 • 2 + 2 • 2 + 4 • 2 = 14

// ... and so on.

// Once we hit `n = 10`, we print the first ten terms as a single line of space-separated
// integers.

// 2. We use a = 5, b = 3, and n = 5 to produce some series 8_0, 8_1, ..., 8_n-1:
// 8_0 = 5 + 1 • 3 = 8
// 8_1 = 5 + 1 • 3 + 2 • 3 = 14
// 8_2 = 5 + 1 • 3 + 2 • 3 + 4 • 3 = 26
// 8_3 = 5 + 1 • 3 + 2 • 3 + 4 • 3 + 8 • 3 = 50
// 8_4 = 5 + 1 • 3 + 2 • 3 + 4 • 3 + 8 • 3 + 8 • 3 = 98

// We then print each element of our series as a single line of space-separated values.

import java.util.*;
import java.io.*;
import java.math.*;

class Solution{
    
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int result = a + 1 * b;
            String resultStr = "" + result + " ";            
            for(int j = 1; j < n; j++){
                double intermidiate = Math.pow(2, j) * b;
                result = result + (int) intermidiate;
                resultStr += result + " ";
            }
            System.out.println(resultStr);
        }
        in.close();
    }
}
