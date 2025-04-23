#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

__attribute__((constructor)) void flush_buf() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void what() {
    __asm__("pop %rdi; ret");
}

void gargantuan() {
    char storage[0x500];
    char tmp[0x200];

    memset(storage, 0, sizeof(storage));

    for (int i = 0; i < 0x5; i++) {
        int total_read = read(0, tmp, 0x200);

        if (total_read <= 0) {
            puts("read error");
            break;
        }

        // check if the input is too large
        if (strlen(tmp) > 0x100) {
            puts("too large");
            break;
        }

        memcpy(storage + strlen(storage), tmp, total_read);
    }

    printf("Oh I'm sorry, did you want this?? Oops, TOO LATE! %p\n", gargantuan);
}


int main(int argc, char* argv[]) {
    puts("Welcome!");
    puts("Enter your input below:");
    gargantuan();
    return 0;
}