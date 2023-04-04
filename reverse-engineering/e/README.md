# e
Level - Hard

Description:
```
#define e "Have"
#define ee " fun"
#define eee "!"

e ee eee

*Note - flag format is `flag{[0-9a-f]}`*

[e.c]
```

## Writeup
When you do all the substitutions, this is what it looks like:

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    char buffer[0x20];
    
    printf("Flag? ");

    scanf("%20s", buffer);

    if (buffer[4] == '{' && buffer[10] == '7' && buffer[0] == 'f' && buffer[18] == '2' && buffer[17] == '5' && buffer[1] == 'l' && buffer[2] == 'a' && buffer[8] == '0' && buffer[19] == '}' && buffer[13] == '2' && buffer[6] == '8' && buffer[5] == 'b' && buffer[9] == 'c' && buffer[11] == '9' && buffer[15] == '4' && buffer[20] == '\0' && buffer[12] == '7' && buffer[3] == 'g' && buffer[16] == '9' && buffer[14] == '9' && buffer[7] == '8') {
        printf("Correct!\n");
    }
    else {
        printf("Incorrect!\n");
    }
    return 0;
}
```

If you pull out the letters and the index in buffer, then you'll get the flag `flag{b880c797294952}`. It may also be easier to just compile and reverse engineer the binary but \o/ have fun!

**Flag** - `flag{b880c797294952}`