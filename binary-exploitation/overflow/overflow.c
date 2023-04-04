#include <stdio.h>

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
}

void vulnerable() {
    int key = 12;
    char buffer[0x30];

    printf("Enter a text please: ");
    scanf("%64s", buffer);

    if (key == 0x34333231) {
        win();
    }
}

int main() {
    vulnerable();
    return 0;
}