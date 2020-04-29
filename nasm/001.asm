; ----------------------------------------------------------------------------------------
; Windows:
;   nasm -f win64 001.asm
;   link /subsystem:console /nodefaultlib /entry:main 001.obj
; Linux:
;   nasm -f elf64 001.asm
;   ld -o 001 001.o -entry=_start --subsystem=console
; ----------------------------------------------------------------------------------------

; NASM uses the following names for general-purpose registers in 64-bit mode:
;     8-bit:  AL/AH, CL/CH, DL/DH, BL/BH, SPL, BPL, SIL, DIL, R8B-R15B
;     16-bit:    AX,    CX,    DX,    BX,  SP,  BP,  SI,  DI, R8W-R15W
;     32-bit:   EAX,   ECX,   EDX,   EBX, ESP, EBP, ESI, EDI, R8D-R15D
;     64-bit:   RAX,   RCX,   RDX,   RBX, RSP, RBP, RSI, RDI,  R8-R15

BITS 32

section .data
    std_out:        equ -11
    cr:             equ 0xD
    lf:             equ 0xA
    msg1:           db "Hello, world!", cr, lf, 0
    msg1_len:       equ $-msg1
    ; s_int:          dd  12345
    s_int:          dd  65
    s_hex:          dd  0xABCD
    s_flt32:        dd  1.234e-30
    s_flt64:        dq  -123.456789e300

; section .bss
;     s_flt32_tmp:    resq 1              ; 64-bit temporary for printing s_flt32

section .text
global  main
    ; C libs
    ; extern  _printf
    ; Win32
    extern _GetStdHandle@4
    extern _WriteFile@20
    extern _ExitProcess@4
    ; Win64
    ; extern GetStdHandle
    ; extern WriteFile
    ; extern ExitProcess

    main:
        ; DWORD  bytes;list
        mov         ebp, esp
        sub         esp, 4
        ; hStdOut = GetstdHandle(STD_OUTPUT_HANDLE)
        push        std_out
        call        _GetStdHandle@4
        mov         ebx, eax

        ; WriteFile(hStdOut, message, length(message), &bytes, 0);
        push        0
        lea         eax, [ebp-4]
        push        eax
        push        dword msg1_len              ; constant pass by value
        push        dword msg1                  ; address of format string
        push        ebx
        call        _WriteFile@20

        ; ExitProcess(0)
        push        0
        call        _ExitProcess@4

        ; Linux
        ; mov         eax, 4      ; 4 - write
        ; mov         ebx, 1      ; 1 - stdout
        ; mov         ecx, msg1
        ; mov         edx, msg1_len
        ; int         0x80
        ; call        exit

    exit:
        ; mov rax, 0    ; exit code
        xor eax, eax    ; exit code
        ret             ; return
        ; int 0x21      ; system call DOS
        ; int 0x80      ; system call Linux
