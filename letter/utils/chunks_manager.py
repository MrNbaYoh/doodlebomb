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

    add_word(chunk_loc)
    add_word(len(chunk))
    chunk_loc += len(chunk)

    add_word(crc.crc32(chunk))

    add_ascii(tag)
    fill(8-len(tag), 0)

def add_chunks():
    for f in chunks:
        incbin(f)
