import java.util.Scanner;

public class Argentina {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int pesos = input.nextInt();
        int dollars = input.nextInt();

        System.out.println(pesos * 0.02 < dollars ? "Pesos" : "Dollars");
    }
}
