## General Information I want to keep about RISC-V

### Instructions:
```
In RISC-V (and many other RISC architectures), these are load instructions that read data from memory into a register. Here’s what each means:

LB: Load Byte
Loads a signed 8-bit value from memory and sign-extends it to 32 bits.

LH: Load Halfword
Loads a signed 16-bit value from memory and sign-extends it to 32 bits. Requires the address to be 2-byte aligned.

LW: Load Word
Loads a 32-bit value from memory. Requires the address to be 4-byte aligned.

LBU: Load Byte Unsigned
Loads an unsigned 8-bit value from memory and zero-extends it to 32 bits.

LHU: Load Halfword Unsigned
Loads an unsigned 16-bit value from memory and zero-extends it to 32 bits. Requires the address to be 2-byte aligned.

Summary Table:

Instruction	Size Loaded	Signed/Unsigned	Alignment Requirement
LB	8 bits	Signed	None
LH	16 bits	Signed	2 bytes
LW	32 bits	Signed	4 bytes
LBU	8 bits	Unsigned	None
LHU	16 bits	Unsigned	2 bytes
```
