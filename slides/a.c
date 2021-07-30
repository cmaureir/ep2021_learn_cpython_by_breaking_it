#include <stdio.h>

float add(int a, float b) {
    return a + b;
}

int main() {
    char msg[] = "hello world";
    int a = 42;
    int x = 3;
    float y = 0.14;
    float z = add(x, y);
    printf("%f", z);
    return 0;
}
