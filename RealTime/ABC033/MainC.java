import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String line = sc.next();

		int res = 0;
		for(String elem : line.split("\\+"))
			res += elem.indexOf("0") < 0 ? 1 : 0;

		System.out.println(res);
	}
}