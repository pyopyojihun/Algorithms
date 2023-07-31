/// Queue(큐)자료구조 선입선출의 자료구조  먼저들어온 데이터가 먼저 나가는것

import java.util.*;
public class queue {
    public static void main(String args[]){
        Queue<Integer> q= new LinkedList<>();

        q.offer(5);//삽입
        q.offer(2);
        q.offer(3);
        q.offer(7);
        q.poll();//삭제
        q.offer(1);
        q.offer(4);
        q.poll();

        while (!q.isEmpty()){
            System.out.print(q.poll()+ " ");
        }
    }
}
