#include <iostream>
using namespace std;

int main() {
    int score;
    int cost;
    cin >> score >> cost;
    cout << (score / 12 >= cost ? "Buy it!" : "Try again") << endl;
    return 0;
}
