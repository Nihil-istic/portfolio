#include <iostream>
#include <string>
using namespace std;

int main() {
    string word;
    cin >> word;

    string reversed;
    string::reverse_iterator ri;

    for (ri = word.rbegin(); ri != word.rend(); ri++) {
        reversed += *ri;
    }

    cout << reversed << endl;

    return 0;
}
