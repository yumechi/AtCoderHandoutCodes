import java.util.Scanner;
 
class Main
{
	public static void main (String[] args)
	{
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		int K = scan.nextInt();
		String s = scan.next();
		
		int MODNUM = 1000000007;
		int[][][] dp = new int[N + 1][K + 2][K + 2];
		dp[0][0][0] = 1;
 
		for(int t = 0; t < N; t++) {
			char c = s.charAt(t);
			for(int i = 0; i < K + 1; i++) {
				for(int j = 0; j < K + 1; j++) {
					if(dp[t][i][j] == 0)
                		continue;
		
        		    if(c == '0' || c == '?') {
                		int nj = j > 0 ? j - 1 : 0;
                		dp[t + 1][i + 1][nj] += dp[t][i][j];
                		if(dp[t + 1][i + 1][nj] >= MODNUM) dp[t + 1][i + 1][nj] -= MODNUM;
        		    }
            		if(c == '1' || c == '?') {
                		int ni = i > 0 ? i - 1 : 0;
                		dp[t + 1][ni][j + 1] += dp[t][i][j];
                		if(dp[t + 1][ni][j + 1] >= MODNUM) dp[t + 1][ni][j + 1] -= MODNUM;
            		}
				}
			}
		}
		
		int res = 0;
		for(int i = 0; i < K + 1; i++) {
			for(int j = 0; j < K + 1; j++) {
				res += dp[N][i][j];
				if(res >= MODNUM) res -= MODNUM;
			}
		}
		
		res %= MODNUM;
		System.out.println(res);
	}
}