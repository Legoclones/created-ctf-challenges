#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

__attribute__((constructor)) void flush_buf() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}


void vuln() {
    char buf[20];
    while (strcmp(buf, "quit") != 0) {
        read(0, buf, 0x100);
        printf(buf);
    }
}


int main(int argc, char* argv[]) {
    vuln();
    return 0;
}