import java.util.Scanner;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
*/
class Solution
{
	static int T;
	static int N;
	static int M;
	static int K;
	static int[][] DRAW = new int[21][5];
	static int AnswerN;

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);

		/*
		   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
		*/
		T = sc.nextInt();
		for (int test_case = 1; test_case <= T; test_case++)
		{
			/*
			   각 테스트 케이스를 표준 입력에서 읽어옵니다.
			*/
			N = sc.nextInt();
			M = sc.nextInt();
			K = sc.nextInt();
			for (int n = 0; n < K; n++)
			{
				DRAW[n][0] = sc.nextInt();
				DRAW[n][1] = sc.nextInt();
				DRAW[n][2] = sc.nextInt();
				DRAW[n][3] = sc.nextInt();
				DRAW[n][4] = sc.nextInt();
			}
//여기에 구현
// DRAW

			// 표준출력(화면)으로 답안을 출력합니다.
			System.out.println("#" + test_case + " " + AnswerN);
		}
		sc.close(); // 사용이 끝난 스캐너 객체를 닫습니다.
	}
}
