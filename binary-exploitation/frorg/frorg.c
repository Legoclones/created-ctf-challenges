#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

__attribute__((constructor)) void flush_buf() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void pop_rdi() {
    __asm__ ( "pop %rdi;"
            "ret" );
}

int main(void) {
    char frorg[32];
    int num;

    // intro
    puts("I love frorggies so much! So much I made this application to store all the frorgie names you want");
    puts("How many frorgies you want to store? ");
    scanf("%d", &num);

    // get frorgy names
    for (int i = 0; i < num; i++) {
        puts("Enter frorgy name: ");
        read(0, frorg+(i*10), 10);
    }

    puts("Thank you!");
    return 0;
}