#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    if (n < 5) {
        cout << "I got this!" << endl;
    } else if (n < 10) {
        cout << "Help me Batman" << endl;
    } else {
        cout << "Good Luck out there!" << endl;
    }

    return 0;
}
