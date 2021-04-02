#include <iostream>
using namespace std;

// Gotham City

/*
You are a police officer, and you get a report of criminal activity! Should you
go on your own, or should you call a superhero to help you fight the crime? If
there are less than 5, you can handle this on your own, if there are 5-10, you
will want to go with Batman for backup, and if there are more than 10, you
should stay where it is safe and let Batman handle this on his own!
*/

// Task

/*
Determine whether you need to call backup based on the total number of
criminals being reported.
*/

// Input Format

/*
An integer that represents the total number of criminals present at the scene.
*/

// Output Format

/*
A string that says 'I got this!', 'Help me Batman', or 'Good Luck out there!'
depending on the scenario.
*/

// Sample Input
// 7

// Sample Output
// 'Help me Batman'

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
