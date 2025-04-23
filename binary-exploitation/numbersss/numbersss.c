#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char length;
char counter;

__attribute__((constructor)) void flush_buf() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void vuln() {
    printf("Free junk: %p\n",printf);

    char buf[0x10];

    printf("How many bytes do you want to read in?\n");
    scanf("%hhd", &length);

    // ensure not greater than 0x10
    if (length > 0x10) {
        printf("Too many bytes!\n");
        exit(1);
    }

    // read in bytes char by char
    counter = 0;
    while (counter != length) {
        read(0, buf + counter, 1);
        counter++;
    }
}


int main(int argc, char* argv[]) {
    vuln();
    return 0;
}