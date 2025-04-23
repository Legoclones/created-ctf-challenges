#include <iostream>
#include <sstream>
#include <cstdlib>
#include <ctime>

int main(int argc, char *argv[]) {
    // Check if a command line argument is provided
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " \"XOR Results\"" << std::endl;
        return 1;
    }

    // Seed with the current time
    std::srand(static_cast<unsigned int>(std::time(nullptr)));

    // Get XOR results from command line argument
    std::string xorResults = argv[1];

    // Parse the XOR results string
    std::istringstream iss(xorResults);
    int xorValue;

    // XOR each integer with a random number
    std::cout << "Decrypted Flag: ";
    while (iss >> xorValue) {
        int randomValue = std::rand() % 256;
        char decryptedChar = static_cast<char>(xorValue ^ randomValue);

        // Print the decrypted character
        std::cout << decryptedChar;
    }
    std::cout << std::endl;

    return 0;
}
