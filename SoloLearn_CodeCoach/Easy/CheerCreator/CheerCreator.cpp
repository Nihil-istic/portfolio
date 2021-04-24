#include <iostream>
using namespace std;

int main() {
    const string A = "High Five";
    const string B = "Ra!";
    const string C = "shh";

    int yards;
    cin >> yards;

    if (yards > 10) {
        cout << A << endl;
    } else if (yards < 1) {
        cout << C << endl;
    } else {
        for (int i = 0; i < yards; i++) {
            cout << B;
        }
        cout << endl;
    }
    return 0;
}
