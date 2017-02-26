include("utils/chunks_manager.py")

put_label("start")

add_ascii("BPK1")
add_word((header_end-header)//0x14) #number of tags/chunks
add_word(0x7)
add_word(end-start)                 #decompressed size

add_word(header_end)

org(0x40)
put_label("header")

set_header_end(header_end)
add_chunk_header('letter_chunks/build/sheet1.bin', "SHEET1")
add_chunk_header('letter_chunks/build/colslt1.bin', "COLSLT1")
add_chunk_header('../res/preview.jpg', 'THUMB2')
add_chunk_header('letter_chunks/build/statin1.bin', 'STATIN1')
add_chunk_header('letter_chunks/build/miistd1.bin', 'MIISTD1')
add_chunk_header('letter_chunks/build/common1.bin', 'COMMON1')
add_chunk_header('letter_chunks/build/dstinf1.bin', 'DSTINF1')
add_chunk_header('letter_chunks/build/rcvinf1.bin', 'RCVINF1')

put_label("header_end")

add_chunks()

put_label("end")
