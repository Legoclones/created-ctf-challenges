# Chicken Writeup
The `chicken.chn` file is an esolang known as (shockingly) [chicken](https://esolangs.org/wiki/Chicken). Each line has the word "chicken" written a certain number of times. If you count up the number of times it says "chicken" on each line, you'll get an opcode. What the opcodes mean can be found in the "Instructions" section of the above link, or explained below. All the program does is make numbers from math, turn those numbers into ASCII characters, and puts it at a certain index of the flag. 

Opcodes:
* 10+ - Push n-10 onto the top of the stack (ie, "chicken" 15 times means to put 5 on the stack)
* 2 - pop the top two numbers off the stack, add them, and push the result back onto the stack
* 3 - pop the top two numbers off the stack, subtract them, and push the result back onto the stack
* 4 - pop the top two numbers off the stack, multiply them, and push the result back onto the stack
* 7 - pops a value off of the top of the stack and stores the character at that index
    * Note - this is different than the intended functionality of the opcode. I purposely misinterpreted this. In my description, I mentioned that "I think I got it wrong", hinting that the code doesn't compile/work - forcing participants to understand the opcodes. 
* 9 - pops a number off of the top of the stack, converts it into ASCII, and pushes the result onto the stack

I wrote a simple Python script (`solve.py`) that will read in the `chicken.chn` file, parse it, run the code based on opcodes, and print out the flag at the end.

**Flag** - `byuctf{th3r3_4r3_3ven_w0rs3_es0l4ngs_but_1m_lazzy}`