import java.util.Scanner;

public class HalloweenCandy {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int houses = input.nextInt();

        System.out.println((int)Math.ceil(2.0 / houses * 100));
    }
}
