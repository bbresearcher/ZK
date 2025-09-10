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

---

## Arithmetic Instructions

| Opcode      | Description                                   |
|-------------|-----------------------------------------------|
| ADD         | Add two registers                             |
| SUB         | Subtract one register from another            |
| XOR         | Bitwise XOR of two registers                  |
| OR          | Bitwise OR of two registers                   |
| AND         | Bitwise AND of two registers                  |
| SLL         | Shift left logical                            |
| SRL         | Shift right logical                           |
| SRA         | Shift right arithmetic                        |
| SLT         | Set if less than (signed)                     |
| SLTU        | Set if less than (unsigned)                   |

---

## Load Instructions

| Opcode      | Description                                   |
|-------------|-----------------------------------------------|
| LB          | Load byte (signed)                            |
| LH          | Load halfword (16 bits, signed)               |
| LW          | Load word (32 bits, signed)                   |
| LBU         | Load byte (unsigned)                          |
| LHU         | Load halfword (16 bits, unsigned)             |

---

## Store Instructions

| Opcode      | Description                                   |
|-------------|-----------------------------------------------|
| SB          | Store byte                                    |
| SH          | Store halfword (16 bits)                      |
| SW          | Store word (32 bits)                          |

---

## Branch Instructions

| Opcode      | Description                                   |
|-------------|-----------------------------------------------|
| BEQ         | Branch if equal                               |
| BNE         | Branch if not equal                           |
| BLT         | Branch if less than (signed)                  |
| BGE         | Branch if greater or equal (signed)           |
| BLTU        | Branch if less than (unsigned)                |
| BGEU        | Branch if greater or equal (unsigned)         |

---

## Jump Instructions

| Opcode      | Description                                   |
|-------------|-----------------------------------------------|
| JAL         | Jump and link (stores return address)         |
| JALR        | Jump and link register                        |

---

## Upper Immediate Instruction

| Opcode      | Description                                   |
|-------------|-----------------------------------------------|
| AUIPC       | Add upper immediate to PC                     |

---

## System Instructions

| Opcode      | Description                                   |
|-------------|-----------------------------------------------|
| ECALL       | Environment call (system call)                |
| EBREAK      | Breakpoint (used for debugging)               |

---

## Multiply/Divide Instructions

| Opcode      | Description                                   |
|-------------|-----------------------------------------------|
| MUL         | Multiply (lower 32 bits)                      |
| MULH        | Multiply high (signed)                        |
| MULHU       | Multiply high (unsigned)                      |
| MULHSU      | Multiply high (signed/unsigned)               |
| DIV         | Divide (signed)                               |
| DIVU        | Divide (unsigned)                             |
| REM         | Remainder (signed)                            |
| REMU        | Remainder (unsigned)                          |

---

## Other/Unimplemented

| Opcode      | Description                                   |
|-------------|-----------------------------------------------|
| UNIMP       | Unimplemented instruction                     |

---
