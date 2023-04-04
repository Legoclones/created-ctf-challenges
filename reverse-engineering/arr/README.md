# Arr
**Level**: Medium

**Points**: 489

**Author**: Justin Applegate

**Description**:
```markdown
Have you ever seen an array in a binary?

[arr]
```

## Writeup
Opening the `main` function in Ghidra will return this decompiled code:

```c
undefined4 main(void)

{
  bool bVar1;
  char *pcVar2;
  basic_ostream *this;
  undefined4 unaff_EBX;
  basic_string<char,std::char_traits<char>,std::allocator<char>> local_d8 [32];
  int local_b8 [4];
  undefined4 local_a8;
  undefined4 local_a4;
  undefined4 local_a0;
  undefined4 local_9c;
  undefined4 local_98;
  undefined4 local_94;
  undefined4 local_90;
  undefined4 local_8c;
  undefined4 local_88;
  undefined4 local_84;
  undefined4 local_80;
  undefined4 local_7c;
  undefined4 local_78;
  undefined4 local_74;
  undefined4 local_70;
  undefined4 local_6c;
  undefined4 local_68;
  undefined4 local_64;
  undefined4 local_60;
  undefined4 local_5c;
  undefined4 local_58;
  undefined4 local_54;
  undefined4 local_50;
  undefined4 local_4c;
  undefined4 local_48;
  undefined4 local_44;
  undefined4 local_40;
  undefined4 local_3c;
  undefined4 local_38;
  undefined4 local_34;
  undefined4 local_30;
  undefined4 local_2c;
  allocator local_1d;
  int local_1c;
  
  local_b8[0] = 99;
  local_b8[1] = 0x74;
  local_b8[2] = 0x66;
  local_b8[3] = 0x7b;
  local_a8 = 99;
  local_a4 = 0x30;
  local_a0 = 0x6e;
  local_9c = 0x67;
  local_98 = 0x72;
  local_94 = 0x34;
  local_90 = 0x74;
  local_8c = 0x75;
  local_88 = 0x6c;
  local_84 = 0x34;
  local_80 = 0x74;
  local_7c = 0x31;
  local_78 = 0x30;
  local_74 = 0x6e;
  local_70 = 0x73;
  local_6c = 0x5f;
  local_68 = 0x79;
  local_64 = 0x30;
  local_60 = 0x75;
  local_5c = 0x5f;
  local_58 = 0x73;
  local_54 = 0x30;
  local_50 = 0x6c;
  local_4c = 0x76;
  local_48 = 0x33;
  local_44 = 100;
  local_40 = 0x5f;
  local_3c = 0x31;
  local_38 = 0x74;
  local_34 = 0x21;
  local_30 = 0x21;
  local_2c = 0x7d;
  std::operator<<((basic_ostream *)std::cout,"Flag> ");
  std::allocator<char>::allocator();
                    /* try { // try from 00102431 to 00102435 has its CatchHandler @ 00102516 */
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
  basic_string<std::allocator<char>>(local_d8,"",&local_1d);
  std::allocator<char>::~allocator((allocator<char> *)&local_1d);
                    /* try { // try from 00102456 to 001024f1 has its CatchHandler @ 00102530 */
  std::getline<char,std::char_traits<char>,std::allocator<char>>
            ((basic_istream *)std::cin,(basic_string *)local_d8);
  local_1c = 0;
  do {
    if (0x23 < local_1c) {
      this = std::operator<<((basic_ostream *)std::cout,"Correct!");
      std::basic_ostream<char,std::char_traits<char>>::operator<<
                ((basic_ostream<char,std::char_traits<char>> *)this,
                 std::endl<char,std::char_traits<char>>);
      bVar1 = true;
LAB_001024f8:
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
                (local_d8);
      if (bVar1) {
        unaff_EBX = 0;
      }
      return unaff_EBX;
    }
    pcVar2 = (char*)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                     operator[]((ulong)local_d8);
    if ((int)*pcVar2 != local_b8[local_1c]) {
      std::operator<<((basic_ostream *)std::cout,"Wrong!");
      unaff_EBX = 0;
      bVar1 = false;
      goto LAB_001024f8;
    }
    local_1c = local_1c + 1;
  } while( true );
}
```

While this may look kind of messy, a loop can be identified towards the bottom beginning with this:

```c
local_1c = 0;
do {
    if (0x23 < local_1c) {
        ...
    }
    local_1c = local_1c + 1;
} while( true );
```

This loop can be rewritten as:

```c
for (local_1c = 0; local_1c < 0x23; local_1c++) {
    ...
}
```

Inside of this loop, the line `if ((int)*pcVar2 != local_b8[local_1c])` is comparing a letter of the inputted flag (represented as `pcVar2`) with an item in the array `local_b8` initialized in the beginning. Further inspection of the array `local_b8` and the initialized values afterwards reveals that each hex value is equivalent to an ASCII character. When all the hex values are converted to ASCII, the flag appears.

The source code can be found in [arr.cpp](arr.cpp).

**Flag** - `ctf{c0ngr4tul4t10ns_y0u_s0lv3d_1t!!}`