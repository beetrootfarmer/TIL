# 1=< N =< 9 ,  N을 받아서 구구단을 출력하는 함수를 만들기 

N = int(input())
for i in range(1,10) : # range(1,10) = 1~9 !!!!!!!
    print(N, "*", i, "=" +(N*i)) # 자바에서 + 로 쓰던거 쉼표로 써야함

# java로 하면
# import java.util.Scanner;
# public class Main {
# 	public static void main(String[] args) {
 
# 		Scanner in = new Scanner(System.in);	
# 		int a = in.nextInt();
		
# 		in.close();		
		
# 		for(int i = 1; i<10;i++) {
# 			System.out.println(a+" * "+i+" = "+(a*i));
# 		}
# 	}
# }
