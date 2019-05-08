import java.util.*;

public class ABC116B {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        Set<Integer> s = new HashSet<>();
        s.add(a);
        int idx = 1;
        while(true) {
            idx++;
            int t = a % 2 == 0 ? (a / 2) : (3 * a + 1);
            if(s.contains(t)) {
                System.out.println(idx);
                break;
            } 
            s.add(t);
            a = t;
        }
    }
}

