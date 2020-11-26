	.text
	.file	"<string>"
	.type	fmt,@object
	.section	.rodata,"a",@progbits
fmt:
	.asciz	"%d\n"
	.size	fmt, 4

	.type	fmt_in,@object
fmt_in:
	.ascii	"%d"
	.size	fmt_in, 2

	.section	".note.GNU-stack","",@progbits
