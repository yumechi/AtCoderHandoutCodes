import java.util.Scanner;

public class Main {
        public static void main(String[] args) {
                Scanner scan = new Scanner(System.in);
                String res = "";
                char x = scan.next().charAt(0);
                String str = scan.next();
                for(int i = 0; i < str.length(); i++) {
                        if(str.charAt(i) != x) {
                                res += str.charAt(i);
                        }
                }

                System.out.println(res);
        }
}
