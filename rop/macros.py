import constants
include("../ropdb/EUR.py")

def sleep(time):
    SET_LR(NOP)
    pop(r0=time, r1=0)
    add_word(SVC_SLEEPTHREAD)

def garbage(n):
    for i in range(n):
        add_word(0xDEAC0DE)

@pop_macro
def POP_R0(r0):
    add_word(POP_R0PC)
    add_word(r0)

@pop_macro
def POP_R1(r1):
    add_word(POP_R1PC)
    add_word(r1)

@pop_macro
def POP_R3(r3):
    add_word(POP_R3PC)
    add_word(r3)

def SET_LR(lr):
    POP_R1(NOP)
    add_word(POP_R4LR_BX_R1)
    add_word(0xDEADC0DE) #r4 garbage
    add_word(lr)

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

@pop_macro
def POP_R4(r4):
    add_word(POP_R4PC)
    add_word(r4)

def mount_sdmc(sdmc_str):
    POP_R0(sdmc_str)
    add_word(FS_MOUNTSDMC + 0x4)
    garbage(3)

def try_get_size(ctx_ptr, out_size):
    pop(r0=ctx_ptr, r1=out_size)
    add_word(FS_TRYGETSIZE + 0x4)
    garbage(2)

def try_open_file(ctx_ptr, file_path_ptr, openflags):
    pop(r0=ctx_ptr, r1=file_path_ptr, r2=openflags)
    add_word(FS_TRYOPENFILE + 0x4)
    garbage(5)

def store(value, addr):
    pop(r0=value, r1=addr)
    add_word(STR_R0R1_POP_R4PC)
    add_word(0xDEADC0DE)

def deref_to_r0(addr):
    POP_R0(addr)
    add_word(LDR_R0R0_POP_R4PC)
    add_word(0xDEADC0DE)

def add_r0(value):
    POP_R4(value)
    add_word(ADD_R0R0R4_POP_R4PC)
    add_word(0xDEADC0DE)

def compare_r0_0():
    add_word(CMP_R0_0_MOVNE_R0_1_POP_R4PC)
    add_word(0xDEADC0DE)

def store_if_equal(value, addr):
    SET_LR(NOP)
    pop(r0=addr, r1=value)
    add_word(STREQ_R1R0_BX_LR)

def deref_and_store(src, dst):
    pop(r0=src, r1=dst)
    add_word(LDR_R0R0_POP_R4PC)
    add_word(0xDEADC0DE)
    add_word(STR_R0R1_POP_R4PC)
    add_word(0xDEADC0DE)

def mov_r9_to_r0():
    POP_R1(NOP)
    add_word(MOV_R0R9_BLX_R1)

def mov_r11_to_r0():
    POP_R1(NOP)
    add_word(MOV_R0R11_BLX_R1)

def mov_r9_to_r0():
    POP_R1(NOP)
    add_word(MOV_R0R9_BLX_R1)

def store_r0(addr):
    POP_R1(addr)
    add_word(STR_R0R1_POP_R4PC)
    add_word(0xDEADC0DE)

@macro
def try_read_file(ctx_ptr, offseth, offsetl, out_bytes_read, size_ptr, dest):
    deref_and_store(ctx_ptr, FilePtr)
    deref_and_store(size_ptr, Size)

    add_word(POP_R1PC)
    put_label("FilePtr")
    add_word(0xDEADC0DE)

    pop(r0=out_bytes_read, r2=offsetl, r3=offseth)
    add_word(FS_TRYREADFILE + 0x4)
    garbage(6)
    add_word(POP_R4R5PC)
    add_word(dest)
    put_label("Size")
    add_word(0xDEADC0DE)

def close_file(ctx_ptr):
    SET_LR(NOP)
    POP_R0(ctx_ptr)
    add_word(FS_CLOSEFILE + 0x4)

def mov_r0_to_r1():
    add_word(MOV_R1R0_POP_R4R5PC)
    garbage(2)

### MACROS FOR STACK BASE ADDRESS AGNOSTIC ROP ###

def make_ptr_to_r0(thread_stack_base_ptr, offset):
    deref_to_r0(thread_stack_base_ptr)
    add_r0(offset)

def load_r0_thread_base(thread_stack_base_ptr, offset):
    deref_to_r0(thread_stack_base_ptr)
    add_r0(offset)
    add_word(LDR_R0R0_POP_R4PC)
    add_word(0xDEADC0DE)

def store_r0_thread_base(thread_stack_base_ptr, offset):
    mov_r0_to_r1()
    deref_to_r0(thread_stack_base_ptr)
    add_r0(offset)
    add_word(STR_R1R0_POP_R4PC)
    add_word(0xDEADC0DE)
