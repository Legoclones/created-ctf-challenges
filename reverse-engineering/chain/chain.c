#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int offsets[45] = {14, 3, 28, 19, 23, 33, 18, 4, 39, 9, 13, 34, 30, 21, 11, 36, 29, 10, 24, 43, 25, 0, 27, 42, 8, 31, 32, 37, 2, 26, 12, 41, 7, 5, 17, 40, 20, 22, 35, 15, 1, 16, 44, 6, 38};
char * base = (char*)0x105ac;

__attribute__((constructor)) void flush_buf() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

int main() {
    int correct[45] = {0xc2,0x9c,0x65,0x83,0x95,0x66,0xfa,0x15,0x5e,0x58,0x2f,0x23,0xac,0x4f,0xa1,0x4c,0x7d,0x1e,0x69,0x80,0x8c,0x4a,0x26,0x5b,0x5f,0x91,0x30,0xcf,0xc0,0x4d,0x97,0x9b,0xba,0x20,0x77,0x4c,0xf5,0xef,0x97,0x96,0x31,0x30,0x8c,0xe2};
    puts("Password? ");

    char buf[0x100];
    fgets(buf, 0xff, stdin);

    if (strlen(buf) != 45) { // aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        puts("Wrong!");
        return 0;
    }

    for (int i = 0; i < 44; i++) {
        char c = *(base + offsets[i]);
        //printf("%x\n", c);
        if ((buf[i] ^ c) != (char) correct[i]) {
            printf("Wrong!");
            return 0;
        }
    }

    puts("Correct!");
    
    return 0;
}