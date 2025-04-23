#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>

#define CBC 0
#define CTR 0
#define ECB 1
#include "aes.h"

char input_buf[1030];

__attribute__((constructor)) void flush_buf() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void parse(uint8_t* decrypted, char* output) {
    char token[16];
    int timezone;

    // ensure decrypted has stuff
    if (decrypted == NULL) {
        memcpy(output, "{\"code\":-2}", 11);
        return;
    }

    // get token and timezone
    char* section = strtok(decrypted, "&");
    while (section != NULL) {
        if (strncmp(section,"t=",2) == 0) {
            sscanf(section, "t=%s", token);
        }
        else if (strncmp(section,"tz=",3) == 0) {
            sscanf(section, "tz=%d", &timezone);
        }
        else {
            memcpy(output, "{\"code\":-1}", 11);
            return;
        }
        section = strtok(NULL, "&");
    }

    memcpy(output, "{\"code\":0}", 11);
    return;
}

void decrypt_aes_ecb(uint8_t* key, uint8_t* decrypted, int num_blocks) {
    for (int i = 0; i < num_blocks; ++i) {
        struct AES_ctx ctx;
        AES_init_ctx(&ctx, key);
        AES_ECB_decrypt(&ctx, decrypted + i*16);
    }
}

int main(int argc, char* argv[]) {
    // generate key
    uint8_t key[] = "0123456789abcdef";

    srand(time(NULL));
    for (int i = 0; i < 16; ++i) {
        key[i] = rand() % 256; // Generate a random byte
    }


    // send them the key
    write(1, key, 16);


    // get their encrypted message
    memset(input_buf, 0, 1030);
    int content_length = read(0, input_buf, 1024);


    // check header
    if (content_length < 15) {
        // too short for a header
        return 1;
    }
    if (input_buf[0] != 0x4c || input_buf[1] != 0x45 || input_buf[7] != 0x47 || input_buf[8] != 0x4f) { // LEGO
        // invalid header
        return 1;
    }

    
    // check payload
    int num_blocks;
    if ((content_length-15) % 16 != 0) {
        // invalid length, must be a multiple of 16
        return 1;
    }
    else {
        num_blocks = (content_length-15) / 16;
    }


    // prep for decryption
    uint8_t decrypted[1030];
    memset(decrypted, 0, 1030);
    for (size_t i = 0; i < content_length-15; ++i) {
        decrypted[i] = (uint8_t)input_buf[i+15];
    }


    // decrypt
    decrypt_aes_ecb(key, decrypted, num_blocks);


    // parse token
    char output[20];
    memset(output, 0, 20);
    parse(decrypted, output);


    // send response
    puts(output);
    

    return 0;
}

void logging() {
    char cmd_buf[0x204];
    memset(cmd_buf, 0, 0x204);

    char cmd[] = "Imagine this is a log message";

    snprintf(cmd_buf, 0x200, "echo '%s'", cmd);
    system(cmd_buf);
}
