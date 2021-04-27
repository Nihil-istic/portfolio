import java.util.Scanner;

public class GothamCity {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int numberOfCriminals = input.nextInt();

        if (numberOfCriminals < 5) {
            System.out.println("I got this!");
        } else if (numberOfCriminals <= 10) {
            System.out.println("Help me Batman");
        } else {
            System.out.println("Good Luck out there!");
        }
    }
}
