#include <iostream>
using namespace std;

int main() {
    int sales;
    cin >> sales;

    int per_month = -1 * (10 * 2000000 + 1000000) + sales * 3000000;

    if (per_month < 0) {
        cout << "Loss" << endl;
    } else if (per_month > 0) {
        cout << "Profit" << endl;
    } else {
        cout << "Broke Even" << endl;
    }

    return 0;
}
