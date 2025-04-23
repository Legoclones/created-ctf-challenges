#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>

int main() {
    // Read the flag from "flag.txt"
    std::ifstream inputFile("flag.txt");
    if (!inputFile.is_open()) {
        std::cerr << "Error opening file 'flag.txt'" << std::endl;
        return 1;
    }

    std::string flag;
    std::getline(inputFile, flag);
    inputFile.close();
    
    // Seed with the current Unix timestamp
    std::srand(static_cast<unsigned int>(std::time(nullptr)));

    // XOR each character with a random number
    std::cout << "XOR Result:     ";
    for (char& c : flag) {
        // Convert char to integer and XOR with a random number
        int randomValue = std::rand() % 256;
        int result = static_cast<int>(c) ^ randomValue;

        // Print the XOR result
        std::cout << result << " ";
    }
    std::cout << std::endl;

    return 0;
}