#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>
#include <ctype.h>

__attribute__((constructor)) void flush_buf() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

int main(int argc, char* argv[]) {
    char input[68];
    char password[68];
    memset(input, 0, sizeof(input));
    memset(password, 0, sizeof(password));

    // get password
    FILE* f = fopen("/ctf/pwd.txt", "r");
    if (!f) {
        puts("Password file not found. Contact an admin if you see this on remote.");
        return 1;
    }
    fgets(password, sizeof(password), f);
    fclose(f);

    // get user input
    printf("Enter the password: ");
    fgets(input, sizeof(input), stdin);

    // compare
    if (memcmp(input, password, 64) != 0) {
        puts("Incorrect password!");
        return 1;
    }

    puts("Welcome to Level 2!");
    puts("Enter your MIPS shellcode below.");
    
    // create RWE segment to store code
    void* code = mmap(0, 0x1000, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    memset(code, 0xff, 0x1000);

    // read shellcode
    char buf[48];
    printf("Shellcode> ");

    int r = read(0, buf, 44); // read does not terminate on null bytes or newlines
    if (r <= 0) {
        printf("read error\n");
        return 1;
    }


    // RUN CHECKS ON SHELLCODE
    for (int i = 0; i < r; i++) {
        if (buf[i] == 0) {
            printf("NULL byte detected in shellcode\n");
            return 1;
        }
        else if (isspace(buf[i])) {
            printf("Whitespace detected in shellcode\n");
            return 1;
        }
    }
    

    // add shellcode to mess up registers
    char mess_registers[108] = {0xff,0xff,0x1f,0x24,0xff,0xff,0x02,0x24,0xff,0xff,0x03,0x24,0xff,0xff,0x04,0x24,0xff,0xff,0x05,0x24,0xff,0xff,0x06,0x24,0xff,0xff,0x07,0x24,0xff,0xff,0x08,0x24,0xff,0xff,0x09,0x24,0xff,0xff,0x0a,0x24,0xff,0xff,0x0b,0x24,0xff,0xff,0x0c,0x24,0xff,0xff,0x0d,0x24,0xff,0xff,0x0e,0x24,0xff,0xff,0x0f,0x24,0xff,0xff,0x18,0x24,0xff,0xff,0x19,0x24,0xff,0xff,0x10,0x24,0xff,0xff,0x11,0x24,0xff,0xff,0x12,0x24,0xff,0xff,0x13,0x24,0xff,0xff,0x14,0x24,0xff,0xff,0x15,0x24,0xff,0xff,0x16,0x24,0xff,0xff,0x17,0x24,0xff,0xff,0x1e,0x24,0xff,0xff,0x1c,0x24};


    // copy shellcode to RWE segment
    memcpy(code, mess_registers, sizeof(mess_registers));
    memcpy(code + sizeof(mess_registers), buf, r);

    // execute shellcode
    ((void (*)())code)();

    return 0;
}