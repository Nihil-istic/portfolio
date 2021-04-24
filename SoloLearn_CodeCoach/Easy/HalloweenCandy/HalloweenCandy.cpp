#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int houses;

    cin >> houses;

    double percentage = (2.0 / houses) * 100;

    cout << ceil(percentage) << endl;
    return 0;
}
