default rel
global main: function
section .text
section .data
section .bss
section .rodata.str1.1

.LC0:                                               ; byte
    db 2FH, 62H, 69H, 6EH, 2FH, 73H, 68H, 00H       ; 0000 _ /bin/sh.

section .text.startup

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


