#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

__attribute__((constructor)) void flush_buf() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void print_flag() {
    FILE* flag_file;
    char c;

    flag_file = fopen("flag.txt", "r");

    if (flag_file != NULL) {
        while ((c = getc(flag_file)) != EOF) {
            printf("%c", c);
        }
        printf("\n");
    }
    else {
        printf("Could not find flag.txt\n");
    }
}

int main() {
    char time_str[12];
    int time_input;
    time_t x;
    time_t current_time;

    // print task
    printf("Task: 'print_flag'\n");
    printf("Description: 'prints out the flag'\n");
    printf("Date: 'undefined'\n\n");
    printf("ERROR - date for 'print_flag' task is not defined\n");
    printf("This task is not available until January 1st, 2024\n\n");
    printf("You may optionally extend this task to be available later\n");
    printf("To specify when you would like to make the task available, specify the number of seconds since January 1st, 1970 UTC\n");

    // get input
    printf("> ");
    scanf("%10s", &time_str);

    // check that the number of seconds isn't before January 1st, 2024
    time_input = atoi(time_str);
    if ((unsigned) time_input < 1704067200) {
        printf("\nERROR - date must be after January 1st, 2024\n");
        return 1;
    }

    // convert to time and print
    x = (time_t)(time_input);
    printf("\nSpecified datetime - %s\n", ctime(&x));

    // get current time and print
    current_time = time(NULL);
    printf("Current datetime - %s\n", ctime(&current_time));

    // check if the specified time is before the current time, and if so print the flag (time > 2147483647 will work)
    if (x < current_time) {
        printf("Time requirement has been met. Running 'print_flag'...\n");
        print_flag();
    }
    else {
        printf("'print_flag' was not run because specified date has not occurred yet. Exiting...\n");
    }
    sleep(1);
    return 0;
}