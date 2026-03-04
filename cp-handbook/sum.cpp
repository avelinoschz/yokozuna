#include <iostream>

int main(){
    int a, b;

    if (std::cin >> a >> b) {
        std::cout << "La suma es: " << (a + b) << std::endl;
    }

    return 0;
}