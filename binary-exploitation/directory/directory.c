#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

__attribute__((constructor)) void flush_buf() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}


void print_menu() {
    puts("1. Add a name");
    puts("2. Remove a name");
    puts("3. Print directory");
    puts("4. Exit");
}

void process_menu() {
    struct {
        int name_count;
        char tmp[0x100];
        int option;
        int index;
        char names[10][20];
    } stack;

    stack.name_count = 0;
    while (stack.option != 4) {
        print_menu();
        printf("> ");
        scanf("%d", &stack.option);
        switch (stack.option) {
            case 1:
                // check if directory is full
                if (stack.name_count >= 10) {
                    puts("Directory is full!");
                    break;
                }

                // get name
                puts("Enter name: ");
                stack.index = read(0, stack.tmp, 0x30);

                // replace newline with nullbyte
                stack.tmp[strcspn(stack.tmp, "\n")] = '\0';

                // put name in directory
                memcpy(stack.names[stack.name_count], stack.tmp, stack.index);

                // increment name count
                stack.name_count++;
                break;
            case 2:
                puts("Enter index: ");
                scanf("%d", &stack.index);

                // check if index is valid
                if (stack.index < 0 || stack.index >= stack.name_count) {
                    puts("Invalid index!");
                    break;
                }

                // remove name from directory
                for (int i = stack.index; i < stack.name_count; i++) {
                    strcpy(stack.names[i], stack.names[i+1]);
                }

                // decrement name count
                stack.name_count--;
                break;
            case 3:
                puts("Printing directory...");
                for (int i = 0; i < stack.name_count; i++) {
                    printf("%d. %s\n", i, stack.names[i]);
                }
                break;
            case 4:
                puts("Exiting...");
                break;
            default:
                puts("Invalid option");
                break;
        }
    }
}

void win() {
    system("/bin/sh");
}


int main(int argc, char* argv[]) {
    process_menu();
    return 0;
}