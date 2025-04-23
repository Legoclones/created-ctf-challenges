// compiled with 'gcc -fno-stack-protector -o src/static -static -no-pie static.c'

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
    char buf[10];
    read(0, buf, 0x100);
}


int main(int argc, char* argv[]) {
    vuln();
    return 0;
}