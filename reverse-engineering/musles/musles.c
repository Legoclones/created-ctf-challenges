#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>

unsigned char payload[] = {104, 231, 224, 32, 32, 32, 32, 104, 231, 231, 32, 32, 32, 32, 104, 169, 198, 104, 231, 226, 6, 32, 32, 32, 47, 37, 104, 152, 161, 26, 210, 56, 201, 121, 148, 166, 104, 153, 195, 99, 167, 91, 189, 31, 239, 211, 104, 17, 44, 4, 104, 25, 36, 4, 47, 165, 133, 32, 32, 32, 123, 104, 152, 170, 25, 221, 50, 190, 151, 94, 206, 104, 153, 216, 70, 154, 118, 252, 200, 45, 165, 104, 17, 44, 4, 104, 25, 36, 4, 47, 165, 162, 32, 32, 32, 123, 104, 152, 131, 74, 120, 247, 242, 87, 74, 242, 104, 153, 234, 38, 20, 132, 173, 54, 56, 151, 104, 17, 44, 4, 104, 25, 36, 4, 85, 67, 123, 104, 152, 102, 252, 231, 98, 38, 53, 71, 164, 104, 153, 57, 142, 130, 3, 74, 89, 62, 251, 104, 17, 232, 104, 25, 36, 4, 85, 101, 123, 104, 152, 230, 92, 195, 231, 220, 52, 32, 32, 104, 153, 149, 43, 172, 139, 176, 73, 32, 32, 104, 17, 44, 4, 104, 25, 36, 4, 85, 6, 123, 104, 231, 224, 33, 32, 32, 32, 104, 231, 231, 33, 32, 32, 32, 104, 158, 99, 79, 82, 82, 69, 67, 84, 1, 118, 104, 169, 198, 104, 231, 226, 40, 32, 32, 32, 47, 37, 104, 231, 224, 28, 32, 32, 32, 104, 231, 231, 32, 32, 32, 32, 47, 37};

int main() {
    // alarm
    alarm(10);

    // Create a new memory segment with RWX permissions
    size_t size = sizeof(payload);
    void *mem = mmap(NULL, size, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (mem == MAP_FAILED) {
        perror("Error mapping memory");
        exit(EXIT_FAILURE);
    }

    // Check if GDB is running
    if (system("pidof gdb > /dev/null") == 0) {
        exit(EXIT_FAILURE);
    }

    // Copy the array of bytes to the memory segment
    memcpy(mem, payload, size);

    // XOR each byte in the memory segment with 32
    unsigned char *ptr = (unsigned char *)mem;
    for (size_t i = 0; i < size; ++i) {
        ptr[i] ^= 32;
    }

    // Run the code in the memory segment
    void (*func)(void) = (void (*)(void))mem;
    func();

    // Clean up: unmap the memory segment
    if (munmap(mem, size) == -1) {
        perror("Error unmapping memory");
        exit(EXIT_FAILURE);
    }

    return 0;
}