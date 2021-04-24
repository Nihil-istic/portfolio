#include <iostream>
using namespace std;

int main() {
    int Pesos;
    int Dollars;

    cin >> Pesos;
    cin >> Dollars;

    cout << (Pesos * 0.02 < Dollars ? "Pesos" : "Dollars") << endl;

    return 0;
}
