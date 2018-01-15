import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt(); 
        
        int ans = 0;
        for(int i = 1; i <= n; i++) {
            int sumDigit = 0;
            int t = i;
            while(t > 0) {
                sumDigit += t % 10;
                t /= 10;
            }
            if(a <= sumDigit && sumDigit <= b) {
                ans += i;
            }
        }

        System.out.println(ans);
    }
}
