public class SelfNum {
 
	public static void main(String[] args) {
 
		boolean[] check = new boolean[10001];	// 1부터 10000이므로
 
		for (int i = 1; i < 10001; i++){
			int n = d(i);
			if(n < 10001){	// 10000 이 넘는 수는 필요가 없음
				check[n] = true; // n이라는 숫자가 check이다 
			}
		}
 
		StringBuilder sb = new StringBuilder();
        
		for (int i = 1; i < 10001; i++) {
			if (!check[i]) {	// false 인 인덱스만 출력
				sb.append(i).append('\n');
			}
		}
		System.out.println(sb);
	}
 
 
 
	public static int d(int n){
		int sum = n;
    
		while(n != 0){
			sum += (n % 10); // 나머지 연산자로 첫 째 자리수 구하기
			n /= 10;	// 10을 나누어 첫 째 자리를 없앤다
		}
    
		return sum;
	}
}    