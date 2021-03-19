#include <iostream>
#include <cmath>
using namespace std;

// Halloween Candy

/*
You go trick or treating with a friend and all but three of the houses that you
visit are giving out candy. One house that you visit is giving out thootbrushes
and the two houses are giving out dollar bills.
*/

// Task

/*
Given the input of the total number of houses that you visited, what is the
percentage chance that one random item pulled from your bag is a dollar bill?
*/

// Input Format

/*
An integer (>=3) representing the total number of houses that you visited.
*/

// Output Format

/*
A percentage value rounded up to the nearest whole number.
*/

int main() {
    int houses;

    cin >> houses;

    double percentage = (2.0 / houses) * 100;

    cout << ceil(percentage) << endl;
    return 0;
}
