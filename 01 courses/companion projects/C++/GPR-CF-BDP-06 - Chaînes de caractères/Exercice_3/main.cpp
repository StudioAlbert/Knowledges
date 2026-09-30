#include <iostream>
#include <string>

bool checkEmpty(std::string& input) {
    // Check pas vide
    if (input.empty()) {
        std::cout << "xxxx = input is empty" << std::endl;
        return false;
    }
    return true;
}

int main() {

    bool input_valid = true;


    do {
        std::string input;
        std::cout << "Saisir le pseudo" << std::endl;
        std::getline(std::cin, input);

        input_valid = checkEmpty(input);

    }while (!input_valid);

    return 0;
}
