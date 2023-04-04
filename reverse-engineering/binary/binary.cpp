#include <string>
#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {

    cout << "Flag> ";

    string input = "";
    getline(cin, input);

    if (input == "ctf{just_0p3n_th1s_1n_n0t3p4d}") {
        cout << "Correct!" << endl;
    }
    else {
        cout << "Wrong :(" << endl;
    }
}