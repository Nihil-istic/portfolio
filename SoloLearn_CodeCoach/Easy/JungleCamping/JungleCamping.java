import java.util.Map;
import java.util.Scanner;

public class JungleCamping {
    public static void main(String[] args) {
        Map<String, String> noiseToAnimal = Map.of(
                "Grr", "Lion",
                "Rawr", "Tiger",
                "Ssss", "Snake",
                "Chirp", "Bird");

        Scanner input = new Scanner(System.in);
        String[] noises = input.nextLine().split(" ");

        String animals = "";

        for (String noise: noises) {
            animals += noiseToAnimal.get(noise) + " ";
        }

        System.out.println(animals);
    }
}
