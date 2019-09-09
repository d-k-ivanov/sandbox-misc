	.file	"002.cpp"
	.text
	.section	.text$_ZNSt9exceptionC2Ev,"x"
	.linkonce discard
	.align 2
	.globl	_ZNSt9exceptionC2Ev
	.def	_ZNSt9exceptionC2Ev;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZNSt9exceptionC2Ev
_ZNSt9exceptionC2Ev:
.LFB64:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	.seh_endprologue
	movq	%rcx, 16(%rbp)
	movq	.refptr._ZTVSt9exception(%rip), %rax
	leaq	16(%rax), %rdx
	movq	16(%rbp), %rax
	movq	%rdx, (%rax)
	nop
	popq	%rbp
	ret
	.seh_endproc
	.section	.text$_ZNSt9bad_allocC1Ev,"x"
	.linkonce discard
	.align 2
	.globl	_ZNSt9bad_allocC1Ev
	.def	_ZNSt9bad_allocC1Ev;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZNSt9bad_allocC1Ev
_ZNSt9bad_allocC1Ev:
.LFB83:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	movq	%rcx, 16(%rbp)
	movq	16(%rbp), %rax
	movq	%rax, %rcx
	call	_ZNSt9exceptionC2Ev
	movq	.refptr._ZTVSt9bad_alloc(%rip), %rax
	leaq	16(%rax), %rdx
	movq	16(%rbp), %rax
	movq	%rdx, (%rax)
	nop
	addq	$32, %rsp
	popq	%rbp
	ret
	.seh_endproc
.lcomm _ZStL8__ioinit,1,1
	.section .rdata,"dr"
.LC0:
	.ascii "new: \0"
.LC1:
	.ascii ", align: \0"
.LC2:
	.ascii ", ptr: \0"
	.text
	.globl	_ZnwySt11align_val_t
	.def	_ZnwySt11align_val_t;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZnwySt11align_val_t
_ZnwySt11align_val_t:
.LFB1863:
	pushq	%rbp
	.seh_pushreg	%rbp
	pushq	%rbx
	.seh_pushreg	%rbx
	subq	$56, %rsp
	.seh_stackalloc	56
	leaq	128(%rsp), %rbp
	.seh_setframe	%rbp, 128
	.seh_endprologue
	movq	%rcx, -48(%rbp)
	movq	%rdx, -40(%rbp)
	movq	-40(%rbp), %rax
	movq	%rax, %rdx
	movq	-48(%rbp), %rcx
	movq	__imp__aligned_malloc(%rip), %rax
	call	*%rax
	movq	%rax, -88(%rbp)
	cmpq	$0, -88(%rbp)
	jne	.L4
	movl	$8, %ecx
	call	__cxa_allocate_exception
	movq	%rax, %rbx
	movq	%rbx, %rcx
	call	_ZNSt9bad_allocC1Ev
	movq	.refptr._ZNSt9bad_allocD1Ev(%rip), %r8
	leaq	_ZTISt9bad_alloc(%rip), %rdx
	movq	%rbx, %rcx
	call	__cxa_throw
.L4:
	leaq	.LC0(%rip), %rdx
	movq	.refptr._ZSt4cout(%rip), %rcx
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movq	-48(%rbp), %rdx
	movq	%rax, %rcx
	call	_ZNSolsEy
	leaq	.LC1(%rip), %rdx
	movq	%rax, %rcx
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movq	%rax, %rcx
	movq	-40(%rbp), %rax
	movq	%rax, %rdx
	call	_ZNSolsEy
	leaq	.LC2(%rip), %rdx
	movq	%rax, %rcx
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movq	%rax, %rcx
	movq	-88(%rbp), %rax
	movq	%rax, %rdx
	call	_ZNSolsEPKv
	movl	$10, %edx
	movq	%rax, %rcx
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_c
	movq	-88(%rbp), %rax
	addq	$56, %rsp
	popq	%rbx
	popq	%rbp
	ret
	.seh_endproc
	.section .rdata,"dr"
.LC3:
	.ascii "delete: \0"
.LC4:
	.ascii ", ptr : \0"
	.text
	.globl	_ZdlPvySt11align_val_t
	.def	_ZdlPvySt11align_val_t;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZdlPvySt11align_val_t
_ZdlPvySt11align_val_t:
.LFB1864:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	movq	%rcx, 16(%rbp)
	movq	%rdx, 24(%rbp)
	movq	%r8, 32(%rbp)
	leaq	.LC3(%rip), %rdx
	movq	.refptr._ZSt4cout(%rip), %rcx
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movq	%rax, %rcx
	movq	24(%rbp), %rax
	movq	%rax, %rdx
	call	_ZNSolsEy
	leaq	.LC1(%rip), %rdx
	movq	%rax, %rcx
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movq	%rax, %rcx
	movq	32(%rbp), %rax
	movq	%rax, %rdx
	call	_ZNSolsEy
	leaq	.LC4(%rip), %rdx
	movq	%rax, %rcx
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movq	16(%rbp), %rdx
	movq	%rax, %rcx
	call	_ZNSolsEPKv
	movl	$10, %edx
	movq	%rax, %rcx
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_c
	movq	16(%rbp), %rcx
	movq	__imp__aligned_free(%rip), %rax
	call	*%rax
	nop
	addq	$32, %rsp
	popq	%rbp
	ret
	.def	__gxx_personality_seh0;	.scl	2;	.type	32;	.endef
	.seh_handler	__gxx_personality_seh0, @unwind, @except
	.seh_handlerdata
.LLSDA1864:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE1864-.LLSDACSB1864
.LLSDACSB1864:
.LLSDACSE1864:
	.text
	.seh_endproc
	.section .rdata,"dr"
.LC5:
	.ascii "delete: align: \0"
	.text
	.globl	_ZdlPvSt11align_val_t
	.def	_ZdlPvSt11align_val_t;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZdlPvSt11align_val_t
_ZdlPvSt11align_val_t:
.LFB1865:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	movq	%rcx, 16(%rbp)
	movq	%rdx, 24(%rbp)
	leaq	.LC5(%rip), %rdx
	movq	.refptr._ZSt4cout(%rip), %rcx
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movq	%rax, %rcx
	movq	24(%rbp), %rax
	movq	%rax, %rdx
	call	_ZNSolsEy
	leaq	.LC4(%rip), %rdx
	movq	%rax, %rcx
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movq	16(%rbp), %rdx
	movq	%rax, %rcx
	call	_ZNSolsEPKv
	movl	$10, %edx
	movq	%rax, %rcx
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_c
	movq	16(%rbp), %rcx
	movq	__imp__aligned_free(%rip), %rax
	call	*%rax
	nop
	addq	$32, %rsp
	popq	%rbp
	ret
	.seh_handler	__gxx_personality_seh0, @unwind, @except
	.seh_handlerdata
.LLSDA1865:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE1865-.LLSDACSB1865
.LLSDACSB1865:
.LLSDACSE1865:
	.text
	.seh_endproc
	.def	__main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
	.align 8
.LC6:
	.ascii "__STDCPP_DEFAULT_NEW_ALIGNMENT__ is \0"
.LC7:
	.ascii "sizeof(Vec3dAVX) is \0"
.LC8:
	.ascii "alignof(Vec3dAVX) is \0"
.LC9:
	.ascii "002.cpp\0"
	.align 8
.LC10:
	.ascii "reinterpret_cast<uintptr_t>(pVec) % alignof(Vec3dAVX) == 0\0"
	.text
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
.LFB1866:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$48, %rsp
	.seh_stackalloc	48
	.seh_endprologue
	call	__main
	leaq	.LC6(%rip), %rdx
	movq	.refptr._ZSt4cout(%rip), %rcx
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movl	$16, %edx
	movq	%rax, %rcx
	call	_ZNSolsEi
	movq	.refptr._ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_(%rip), %rdx
	movq	%rax, %rcx
	call	_ZNSolsEPFRSoS_E
	leaq	.LC7(%rip), %rdx
	movq	.refptr._ZSt4cout(%rip), %rcx
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movl	$32, %edx
	movq	%rax, %rcx
	call	_ZNSolsEy
	movl	$10, %edx
	movq	%rax, %rcx
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_c
	leaq	.LC8(%rip), %rdx
	movq	.refptr._ZSt4cout(%rip), %rcx
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movl	$32, %edx
	movq	%rax, %rcx
	call	_ZNSolsEy
	movl	$10, %edx
	movq	%rax, %rcx
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_c
	movl	$32, %edx
	movl	$320, %ecx
	call	_ZnaySt11align_val_t
	movq	%rax, -8(%rbp)
	movq	-8(%rbp), %rax
	andl	$31, %eax
	testq	%rax, %rax
	je	.L11
	movl	$68, %r8d
	leaq	.LC9(%rip), %rdx
	leaq	.LC10(%rip), %rcx
	call	_assert
.L11:
	cmpq	$0, -8(%rbp)
	je	.L12
	movq	-8(%rbp), %rax
	movl	$32, %edx
	movq	%rax, %rcx
	call	_ZdaPvSt11align_val_t
.L12:
	movl	$40, %ecx
	call	_Znay
	movq	%rax, -16(%rbp)
	cmpq	$0, -16(%rbp)
	je	.L13
	movq	-16(%rbp), %rax
	movq	%rax, %rcx
	call	_ZdaPv
.L13:
	movl	$0, %eax
	addq	$48, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.globl	_ZTISt9bad_alloc
	.section	.rdata$_ZTISt9bad_alloc,"dr"
	.linkonce same_size
	.align 8
_ZTISt9bad_alloc:
	.quad	_ZTVN10__cxxabiv120__si_class_type_infoE+16
	.quad	_ZTSSt9bad_alloc
	.quad	_ZTISt9exception
	.globl	_ZTSSt9bad_alloc
	.section	.rdata$_ZTSSt9bad_alloc,"dr"
	.linkonce same_size
	.align 8
_ZTSSt9bad_alloc:
	.ascii "St9bad_alloc\0"
	.globl	_ZTISt9exception
	.section	.rdata$_ZTISt9exception,"dr"
	.linkonce same_size
	.align 8
_ZTISt9exception:
	.quad	_ZTVN10__cxxabiv117__class_type_infoE+16
	.quad	_ZTSSt9exception
	.globl	_ZTSSt9exception
	.section	.rdata$_ZTSSt9exception,"dr"
	.linkonce same_size
	.align 8
_ZTSSt9exception:
	.ascii "St9exception\0"
	.text
	.def	__tcf_0;	.scl	3;	.type	32;	.endef
	.seh_proc	__tcf_0
__tcf_0:
.LFB2384:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	leaq	_ZStL8__ioinit(%rip), %rcx
	call	_ZNSt8ios_base4InitD1Ev
	nop
	addq	$32, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.def	_Z41__static_initialization_and_destruction_0ii;	.scl	3;	.type	32;	.endef
	.seh_proc	_Z41__static_initialization_and_destruction_0ii
_Z41__static_initialization_and_destruction_0ii:
.LFB2383:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	movl	%ecx, 16(%rbp)
	movl	%edx, 24(%rbp)
	cmpl	$1, 16(%rbp)
	jne	.L18
	cmpl	$65535, 24(%rbp)
	jne	.L18
	leaq	_ZStL8__ioinit(%rip), %rcx
	call	_ZNSt8ios_base4InitC1Ev
	leaq	__tcf_0(%rip), %rcx
	call	atexit
.L18:
	nop
	addq	$32, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.def	_GLOBAL__sub_I__ZnwySt11align_val_t;	.scl	3;	.type	32;	.endef
	.seh_proc	_GLOBAL__sub_I__ZnwySt11align_val_t
_GLOBAL__sub_I__ZnwySt11align_val_t:
.LFB2385:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	movl	$65535, %edx
	movl	$1, %ecx
	call	_Z41__static_initialization_and_destruction_0ii
	nop
	addq	$32, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.section	.ctors,"w"
	.align 8
	.quad	_GLOBAL__sub_I__ZnwySt11align_val_t
	.ident	"GCC: (x86_64-posix-seh-rev0, Built by MinGW-W64 project) 8.1.0"
	.def	__cxa_allocate_exception;	.scl	2;	.type	32;	.endef
	.def	__cxa_throw;	.scl	2;	.type	32;	.endef
	.def	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc;	.scl	2;	.type	32;	.endef
	.def	_ZNSolsEy;	.scl	2;	.type	32;	.endef
	.def	_ZNSolsEPKv;	.scl	2;	.type	32;	.endef
	.def	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_c;	.scl	2;	.type	32;	.endef
	.def	_ZNSolsEi;	.scl	2;	.type	32;	.endef
	.def	_ZNSolsEPFRSoS_E;	.scl	2;	.type	32;	.endef
	.def	_ZnaySt11align_val_t;	.scl	2;	.type	32;	.endef
	.def	_assert;	.scl	2;	.type	32;	.endef
	.def	_ZdaPvSt11align_val_t;	.scl	2;	.type	32;	.endef
	.def	_Znay;	.scl	2;	.type	32;	.endef
	.def	_ZdaPv;	.scl	2;	.type	32;	.endef
	.def	_ZNSt8ios_base4InitD1Ev;	.scl	2;	.type	32;	.endef
	.def	_ZNSt8ios_base4InitC1Ev;	.scl	2;	.type	32;	.endef
	.def	atexit;	.scl	2;	.type	32;	.endef
	.section	.rdata$.refptr._ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_, "dr"
	.globl	.refptr._ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	.linkonce	discard
.refptr._ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_:
	.quad	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	.section	.rdata$.refptr._ZSt4cout, "dr"
	.globl	.refptr._ZSt4cout
	.linkonce	discard
.refptr._ZSt4cout:
	.quad	_ZSt4cout
	.section	.rdata$.refptr._ZNSt9bad_allocD1Ev, "dr"
	.globl	.refptr._ZNSt9bad_allocD1Ev
	.linkonce	discard
.refptr._ZNSt9bad_allocD1Ev:
	.quad	_ZNSt9bad_allocD1Ev
	.section	.rdata$.refptr._ZTVSt9bad_alloc, "dr"
	.globl	.refptr._ZTVSt9bad_alloc
	.linkonce	discard
.refptr._ZTVSt9bad_alloc:
	.quad	_ZTVSt9bad_alloc
	.section	.rdata$.refptr._ZTVSt9exception, "dr"
	.globl	.refptr._ZTVSt9exception
	.linkonce	discard
.refptr._ZTVSt9exception:
	.quad	_ZTVSt9exception
