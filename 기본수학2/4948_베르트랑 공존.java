package 기본수학2;

import java.util.Scanner;

public class Main{

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        while(true){
            int n = scan.nextInt();
            int cnt = 0;
            if(n == 0) break;

            for(int i = n+1; i<=2*n; i++){
                int result = 0;
                int half = (int)Math.sqrt(i);
                if (i==1) result++;

                for(int j=2; j<=half;j++){
                    if(i%j==0){
                        result++;
                        break;
                    }
                }
                if(result==0){
                    cnt++;
                }
            }
            System.out.print(cnt);
        }
        scan.close();
    }
}