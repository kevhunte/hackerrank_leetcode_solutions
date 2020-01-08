import java.util.*;
class Solution{
	
	public static void main(String []argh)
	{
		Scanner sc = new Scanner(System.in);
		while (sc.hasNext()) {
			String input=sc.next();
            //Complete the code
            String ans = processInput(input);
            System.out.println(ans);
	    }
    }

    private static String processInput(String input){
        //push on left brackets, pop on right brackets.
        //if right doesn't match top of stack, not balanced. Immediately fail
        //if the stack is empy it's true
        String ans = "true";
        Stack<Character> stack = new Stack<Character>();

        for(char i : input.toCharArray()){
            if (i == '[' || i == '{' || i == '(' ){
                stack.push(i);
            }
            else if( i == ')' || i == '}' || i == ']'){
                if(stack.size() == 0){//if this char comes first, not even
                    return "false";
                }
                char top = stack.peek();
                if((top == '(' && i == ')')||(top == '{' && i == '}')||(top == '[' && i == ']')){//check matching pairs here. top and i => () or {} or []
                    stack.pop();
                }
                else{
                    return "false";
                }
            }
        }
        //if there's still values in the stack, then not all matches found. Fail
        if(stack.size() > 0){
            return "false";
        }
        else{
            return "true";
        }
        
    }
}




