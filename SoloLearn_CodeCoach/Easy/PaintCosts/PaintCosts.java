import java.util.Scanner;

public class PaintCosts {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int colors = input.nextInt();

        System.out.println((int)Math.round(1.1 * (5 * colors + 40)));
    }
}
