import java.util.Scanner;

public class SkeeBall {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int score = input.nextInt();
        int cost = input.nextInt();

        System.out.println(score / 12 >= cost ? "Buy it!" : "Try again");
    }
}
