import crc

chunks = []

chunk_loc = None
def set_header_end(header_end):
    global chunk_loc
    chunk_loc = header_end

def add_chunk_header(file, tag):
    global chunk_loc
    chunks.append(file)

    f = open(file, 'rb')
    chunk = f.read()
    f.close()

    add_word(chunk_loc) # chunk header starts with the offset of the chunk in the file
    add_word(len(chunk)) # then its length
    add_word(crc.crc32(chunk)) # then its CRC32

    add_ascii(tag) # to finish its tag
    fill(8-len(tag), 0) # fill the space until the string is 8 bytes long

    chunk_loc += (len(chunk) + 0x3) & (~0x3) # chunks are 4 bytes aligned to prevent potential crashes (with aligned memcpy for example)


def add_chunks():
    for f in chunks:
        incbin(f)
        align(4)
