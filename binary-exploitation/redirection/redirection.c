#include <stdio.h>
#include <stdlib.h>

char flag[0xff];

// this ensures that you don't need to flush stdout when calling printf
__attribute__((constructor)) void flush_buf() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void vulnerable() {
    int one = 1;
    int two = 2;
    char buffer[0x20];

    // read flag
    
    FILE* flag_file;
    flag_file = fopen("flag.txt", "r");

    if (flag_file != NULL) {
        fscanf(flag_file, "%s", flag);
    }
    else {
        printf("Could not find flag.txt\n");
        exit(1);
    }

    // impossible scenario
    if (one == two)  {
        printf("Your flag is - %s\n", flag);
    }

    printf("Enter your name: ");
    scanf("%s", buffer);
}

int main() {
    printf("Calling 'vulnerable'...\n");
    vulnerable();
    return 0;
}