from constants import *
include("macros.py")
set_mem_offset(STAGE0_OFFSET)

incbin("build/rop_stage0_base.bin")
put_label("end")

#this should be executed only if the rop file is not found on the SD card
#it basically increases the stack pointer until the args of the parse function are reached in the stack
#then it jumps to the return instrcutions of the parse function (mov r0, #0 and pop {...})
#thus this simulates a return false and the game displays a message saying the letter is corrupted
fill(PARSE_LETTER_STACK_RETURN_OFFSET-4-end, NOP, 4) #execute NOP until SP is 4 bytes before the parse function args
add_word(PARSE_RETURN) #return instrcutions of the parse function
