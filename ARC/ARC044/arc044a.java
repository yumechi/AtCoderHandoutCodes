import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        if(n > 5 && (n % 2 == 0 || n % 3 == 0 || n % 5 == 0)) {
            System.out.println("Not Prime");
        } else {
            if(n > 5) {
                System.out.println("Prime");
            } else {
                System.out.println(n == 2 || n == 3 || n == 5 ? "Prime" : "Not Prime");
            }
        }
    }
}
