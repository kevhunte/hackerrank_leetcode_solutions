import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        //ArrayList<Integer> arraylist = new ArrayList<Integer>();
        Scanner in = new Scanner(System.in);
        String message = in.next();//turn to chararray, iterate through
        int shiftBy = in.nextInt();
        long ans = 0;
        for(char m : message.toCharArray()){
            ans*=10;//shift nums down
            int num = Character.getNumericValue(m);//convert to int from char
            ans += (num + shiftBy) % 10;//shifts each
        }
        //for()
        System.out.println(ans);//print vals once shifted
    }
}
