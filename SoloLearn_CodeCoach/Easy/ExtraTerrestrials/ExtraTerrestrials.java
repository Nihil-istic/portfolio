import java.util.Scanner;

public class ExtraTerrestrials {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String word = input.next();
        String reversed_word = "";

        for (int i = word.length() - 1; i >= 0; i--) {
            reversed_word += word.charAt(i);
        }

        System.out.println(reversed_word);
    }
}
