#include <iostream>
#include <string>
using namespace std;

int main() {
    const string YES = "give away";
    const string NO = "eat them yourself";

    int siblings;
    int popsicles;

    cin >> siblings >> popsicles;

    cout << (popsicles % siblings == 0 ? YES : NO) << endl;
    return 0;
}
