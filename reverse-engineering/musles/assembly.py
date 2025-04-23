from pwn import *

context.arch = 'amd64'

code = asm("""
// byuctf{ur_GDB_skills_are_really_swoll}

// read 38 bytes onto the stack
mov rax, 0
mov rdi, 0
mov rsi, rsp
mov rdx, 38
syscall

// put "byuctf{u" into rax
mov rax, 0x86b459e918f23a81
mov rcx, 0xf3cf3f9d7b8743e3
xor QWORD PTR [rsp], rcx
           
// check if the first 8 bytes are correct
cmp QWORD PTR [rsp], rax
jne fail
pop rbx
           
// put "r_GDB_sk" into rax
mov rax, 0xee7eb79e12fd398a
mov rcx, 0x850de8dc56ba66f8
xor QWORD PTR [rsp], rcx
           
// check if the next 8 bytes are correct
cmp QWORD PTR [rsp], rax
jne fail
pop rbx
           
// put "ills_are" into rax
mov rax, 0xd26a77d2d7586aa3
mov rcx, 0xb718168da43406ca
xor QWORD PTR [rsp], rcx
           
// check if the next 8 bytes are correct
cmp QWORD PTR [rsp], rax
jne fail
pop rbx
           
// put "_really_" into rax
mov rax, 0x8467150642c7dc46
mov rcx, 0xdb1e796a23a2ae19
xor rax, rcx
           
// check if the next 8 bytes are correct
cmp QWORD PTR [rsp], rax
jne fail
pop rbx

// put "swoll}" into rax
mov rax, 0x14fcc7e37cc6
mov rcx, 0x6990ab8c0bb5
xor QWORD PTR [rsp], rcx

// check if the next 4 bytes are correct
cmp QWORD PTR [rsp], rax
jne fail
pop rbx
           
// print "Correct!"
mov rax, 1
mov rdi, 1
mov rsi, 0x2174636572726f43
push rsi
mov rsi, rsp
mov rdx, 8
syscall

           
// if fail, exit
fail:
    mov rax, 60
    mov rdi, 0
    syscall
""")

print([x^32 for x in code])