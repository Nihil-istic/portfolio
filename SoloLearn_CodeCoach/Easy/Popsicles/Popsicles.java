import java.util.Scanner;

public class Popsicles {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int siblings = input.nextInt();
        int popsicles = input.nextInt();

        System.out.println(popsicles % siblings == 0 ? "give away" : "eat them yourself");
    }
}
