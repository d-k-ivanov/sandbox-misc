; Disassembly of file: exec_shell.64.o
; Mon Feb 25 01:33:34 2019
; Mode: 64 bits
; Syntax: YASM/NASM
; Instruction set: 8086, x64

default rel
global main: function

extern execve                                           ; near
extern _GLOBAL_OFFSET_TABLE_                            ; byte

SECTION .text   align=1 execute                         ; section number 1, code
SECTION .data   align=1 noexecute                       ; section number 2, data
SECTION .bss    align=1 noexecute                       ; section number 3, bss
SECTION .rodata.str1.1 align=1 noexecute                ; section number 4, const

.LC0:                                                   ; byte
        db 2FH, 62H, 69H, 6EH, 2FH, 73H, 68H, 00H       ; 0000 _ /bin/sh.


SECTION .text.startup align=16 execute                  ; section number 5, code

main:   ; Function begin
        sub     rsp, 24                                 ; 0000 _ 48: 83. EC, 18
        lea     rdi, [rel .LC0]                         ; 0004 _ 48: 8D. 3D, 00000000(rel)
        xor     edx, edx                                ; 000B _ 31. D2
        mov     rsi, rsp                                ; 000D _ 48: 89. E6
        mov     qword [rsp], rdi                        ; 0010 _ 48: 89. 3C 24
        mov     qword [rsp+8H], 0                       ; 0014 _ 48: C7. 44 24, 08, 00000000
        call    execve                                  ; 001D _ E8, 00000000(PLT r)
        add     rsp, 24                                 ; 0022 _ 48: 83. C4, 18
        ret                                             ; 0026 _ C3
; main End of function


