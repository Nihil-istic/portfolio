import java.util.Scanner;

public class Hovercraft {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int sales = input.nextInt();

        int perMonth = (10 * -2_000_000 - 1_000_000) + sales * 3_000_000;

        if (perMonth < 0) {
            System.out.println("Loss");
        } else if (perMonth > 0) {
            System.out.println("Profit");
        } else {
            System.out.println("Broke Even");
        }

    }
}
