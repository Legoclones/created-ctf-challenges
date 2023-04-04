#include <string>
#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
    string chars = "asdghkashdfclkamsdfjalxsdkjfxhcaksvjnalsckuqpoiewt";
    cout << "Welcome to the Immersive Cybersecurity Experience." << endl;

    string testval = "";
    for (unsigned int i = 0; i < (1050/3); i+=7) {
        int index = i;
        while (index >= chars.length()) {
            index -= chars.length();
        }
        testval += chars[index];
        cout << "*";
    }
    cout << endl;

    cout << "This is the login form to gain access to the internal interface." << endl << endl;

    cout << "Please enter the password: ";

    string flag = "";
    getline(cin, flag);

    int values[50] = {0x02, 0x07, 0x07, 0x17, 0x0A, 0x0F, 0x03, 0x11, 0x13, 0x18, 0x04, 0x39, 0x13, 0x05, 0x10, 0x5A, 0x02, 0x0F, 0x0F, 0x01, 0x0A, 0x0B, 0x0F, 0x3C, 0x57, 0x5F, 0x34, 0x12, 0x36, 0x0F, 0x07, 0x16, 0x00, 0x3E, 0x0F, 0x07, 0x05, 0x08, 0x1F, 0x16, 0x0D, 0x06, 0x15, 0x5F, 0x37, 0x03, 0x17, 0x57, 0x51, 0x0C};

    if (flag.length() > 50) {
        cout << "Too long" << endl;
        return 0;
    }
    else if (flag.length() < 50) {
        cout << "Too short" << endl;
        return 0;
    }

    string test = "";
    for (unsigned int j = 0; j < testval.length(); j++) {
        test += (values[j] ^ flag[j]);
    }

    if (test==testval) {
        cout << "Success!" << endl;
    }
    else {
        cout << "Incorrect :(" << endl;
    }
}