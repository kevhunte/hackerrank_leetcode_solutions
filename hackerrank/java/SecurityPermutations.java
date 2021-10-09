import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        //ArrayList<Integer> arrayList = new ArrayList<Integer>();
        Scanner in = new Scanner(System.in);
        int len = in.nextInt();
        int nums[] = new int[len];
        int index = 0;
        while(in.hasNextInt())
            nums[index++] = in.nextInt();//collects all data
        
        for(int a:nums)//correctly collected
            System.out.println(nums[a-1]);//print the number at the index given
    }
}
