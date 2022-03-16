class Solution {
    public int solution(int money, int[] costs) {
        int answer = 0;
        // money(만든 돈의 가치)를 만드는데 필요한 '생산비용'이 answer
        // money와 costs가 입력된다
        // 1999
        // int f = ((money/100)*100)/500;
        // int e = (((money/100)*100)-(500*f))/100;
        // int d = ((money%100)*100)/50;
        // int c = (((money%100)*100) - (50*d))/10;
        // int b = (((money%100)*100) - (50*d)- (10*c))/5;
        // int a = ((money%100)*100) - (50*d)- (10*c) - (5*b);
        int f = ((money/100)*100)/500; //1999일때 3
        int e = (((money/100)*100)-(500*f))/100; //1999일때 4
        int d = (money%100)/50;//1999일때 1 , 근데 % 소수점살면 0.99/50인데?
        int c = ((money%100) - (50*d))/10; //1999일때 4
        int b = ((money%100) - (50*d)- (10*c))/5; //1999일때 1?!?!
        int a = (money%100) - (50*d)- (10*c) - (5*b);
        // money = 1*a + 5*b + 10*c + 50*d + 100*e + 500*f;
        
                answer += costs[0]*a;
                answer += costs[1]*b;
                answer += costs[2]*c;
                answer += costs[3]*d;
                answer += costs[4]*e;
                answer += costs[5]*f;
        return answer;   
    }
}


// 테스트 1
// 입력값 〉
// 4578, [1, 4, 99, 35, 50, 1000]
// 기댓값 〉
// 2308
// 실행 결과 〉
// 실행한 결괏값 9240이(가) 기댓값 2308와(과) 다릅니다.
// 테스트 2
// 입력값 〉
// 1999, [2, 11, 20, 100, 200, 600]
// 기댓값 〉
// 2798
// 실행 결과 〉
// 실행한 결괏값 2799이(가) 기댓값 2798와(과) 다릅니다.