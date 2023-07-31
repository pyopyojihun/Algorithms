/// 스택 선입후출 구조

import java.util.*;

public class stack {
    public static void main(String args[]){
        Stack<Integer> s=new Stack<>();
        for(int i=0;i<=4;i++){
            s.push((int)(Math.random()*10000)%10);
        }
        while(!s.empty()){
            System.out.print(s.peek()+" ");
            s.pop();
        }
    }
}






