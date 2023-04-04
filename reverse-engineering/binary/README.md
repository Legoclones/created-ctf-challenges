# Binary
**Level**: Easy

**Points**: 397

**Author**: Justin Applegate

**Description**:
```markdown
Can you reverse the compiled code to get the flag?

[binary]
```

## Writeup
Opening the `main` function in Ghidra will return this decompiled code:

```c

undefined8 main(void)

{
  bool bVar1;
  basic_ostream *pbVar2;
  basic_string<char,std::char_traits<char>,std::allocator<char>> local_48 [47];
  allocator local_19 [9];
  
  std::operator<<((basic_ostream *)std::cout,"Flag> ");
  std::allocator<char>::allocator();
                    /* try { // try from 00102303 to 00102307 has its CatchHandler @ 001023af */
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
  basic_string<std::allocator<char>>(local_48,"",local_19);
  std::allocator<char>::~allocator((allocator<char> *)local_19);
                    /* try { // try from 00102325 to 0010239b has its CatchHandler @ 001023c9 */
  std::getline<char,std::char_traits<char>,std::allocator<char>>
            ((basic_istream *)std::cin,(basic_string *)local_48);
  bVar1 = std::operator==((basic_string *)local_48,"ctf{just_0p3n_th1s_1n_n0t3p4d}");
  if (bVar1 == false) {
    pbVar2 = std::operator<<((basic_ostream *)std::cout,"Wrong :(");
    std::basic_ostream<char,std::char_traits<char>>::operator<<
              ((basic_ostream<char,std::char_traits<char>> *)pbVar2,
               std::endl<char,std::char_traits<char>>);
  }
  else {
    pbVar2 = std::operator<<((basic_ostream *)std::cout,"Correct!");
    std::basic_ostream<char,std::char_traits<char>>::operator<<
              ((basic_ostream<char,std::char_traits<char>> *)pbVar2,
               std::endl<char,std::char_traits<char>>);
  }
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
            (local_48);
  return 0;
}
```

The flag can be seen in plaintext in the code. In addition, using the Linux command `strings` or opening the file in any editor will show the flag in the text.

The source code can be found in [binary.cpp](binary.cpp).

**Flag** - `ctf{just_0p3n_th1s_1n_n0t3p4d}`