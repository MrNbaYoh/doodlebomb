include("../utils/chunks_manager.py")

put_label("start")

add_ascii("BPK1")
add_word((header_end-header)//0x14) #number of tags/chunks
add_word(0x7)
add_word(end-start)                 #decompressed size

add_word(header_end)

org(0x40)
put_label("header")

set_header_end(header_end)
add_chunk_header('statin1_chunks/build/stahed1.bin', 'STAHED1')
add_chunk_header('statin1_chunks/build/stbard1.bin', 'STBARD1')

put_label("header_end")

add_chunks()

put_label("end")
