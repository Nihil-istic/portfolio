#include <iostream>
#include <string>
#include <map>

int main() {
    std::map<std::string, std::string> noiseToAnimal = {
        {"Grr", "Lion"}, {"Rawr", "Tiger"},
        {"Ssss", "Snake"}, {"Chirp", "Bird"}
    };

    std::string input;
    while (std::cin >> input) {
        auto it = noiseToAnimal.find(input);
        std::string output = it != noiseToAnimal.end() ? it->second : "";
        std::cout << output << ' ';
    }
    return 0;
}
