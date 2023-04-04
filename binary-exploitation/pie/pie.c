#include <stdio.h>
#include <stdlib.h>

// this ensures that you don't need to flush stdout when calling printf
__attribute__((constructor)) void flush_buf() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void win() {
    FILE* flag_file;
    char c;

    flag_file = fopen("flag.txt", "r");

    if (flag_file != NULL) {
        printf("Your flag is - ");
        while ((c = getc(flag_file)) != EOF) {
            printf("%c", c);
        }
        printf("\n");
    }
    else {
        printf("Could not find flag.txt\n");
    }
    exit(0);
}

void vulnerable() {
    char buffer[0x20];

    printf("Vulnerable is located at %p\n",vulnerable);

    printf("Enter your name: ");
    scanf("%s", buffer);
}

int main() {
    printf("Calling 'vulnerable'...\n");
    vulnerable();
    return 0;
}