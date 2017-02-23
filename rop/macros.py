import constants
include("../ropdb/EUR.py")

@pop_macro
def POP_R0(r0):
    add_word(POP_R0PC)
    add_word(r0)

@pop_macro
def POP_R1(r1):
    add_word(POP_R1PC)
    add_word(r1)

@pop_macro
def SET_LR(r14):
    POP_R1(NOP)
    add_word(POP_R4LR_BX_R1)
    add_word(0xDEADC0DE) #r4 garbage
    add_word(r14)

@pop_macro
def POP_R2R3R4R5R6(r2, r3, r4, r5, r6):
    add_word(POP_R2R3R4R5R6PC)
    add_word(r2)
    add_word(r3)
    add_word(r4)
    add_word(r5)
    add_word(r6)

@pop_macro
def POP_R4R5R6R7R8R9R10R11(r4, r5, r6, r7, r8, r9, r10, r11):
    add_word(POP_R4R5R6R7R8R9R10R11PC)
    add_word(r4)
    add_word(r5)
    add_word(r6)
    add_word(r7)
    add_word(r8)
    add_word(r9)
    add_word(r10)
    add_word(r11)

@pop_macro
def POP_R4R5R6R7R8R9R10R11(r4, r5, r6, r7, r8, r9, r10, r11, r12):
    add_word(POP_R4R5R6R7R8R9R10R11R12PC)
    add_word(r4)
    add_word(r5)
    add_word(r6)
    add_word(r7)
    add_word(r8)
    add_word(r9)
    add_word(r10)
    add_word(r11)
    add_word(r12)
