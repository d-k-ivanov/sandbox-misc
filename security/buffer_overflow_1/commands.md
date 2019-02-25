# Commands

## Disable address randomization

```bash
sudo bash -c 'echo "kernel.randomize_va_space = 0" >> /etc/sysctl.conf'
sudo sysctl -p
cat /proc/sys/kernel/randomize_va_space   # Should be '0'
```

## Alternative

```bash
sudo bash -c 'echo "0" > /proc/sys/kernel/randomize_va_space'
cat /proc/sys/kernel/randomize_va_space   # Should be '0'
```

## Un limit

```bash
ulimit -c unlimited
ulimit -c
# verify "unlimited"
```

##  compile the code

```bash 
rm -f vuln && gcc -z execstack -fno-stack-protector -g -m64 vuln.c -o vuln
rm -f vuln && gcc -z execstack -fno-stack-protector -g -m64 vuln2.c -o vuln2
```

## GDB Env

```bash
chmod +x envexec.sh
./envexec.sh -d vuln
```

## Execute

```bash
./envexec.sh -d /root/vuln $(python -c 'print("Hello")')
```

##  Run GDB

```bash
gdb vuln
```

## ASM

### Hello asm

```bash
nasm -f elf64 hello.64.s -o hello.64.o &&  ld hello.64.o -o hello.64.bin
rm -f hello.64.o hello.64.bin && nasm -f elf64 hello.64.s -o hello.64.o &&  ld hello.64.o -o hello.64.bin
for i in $(objdump -d ./hello.64.o | grep "^ " | cut -f2); do echo -n '\x'$i; done; echo
"\xb8\x01\x00\x00\x00\xbf\x01\x00\x00\x00\x48\xbe\x00\x00\x00\x00\x00\x00\x00\x00\xba\x0e\x00\x00\x00\x0f\x05\xb8\x3c\x00\x00\x00\xbf\x00\x00\x00\x00\x0f\x05"
```

### Run shell 1

```py
"\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05"
```
