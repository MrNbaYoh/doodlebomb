all: statin1_chunk

statin1_chunk: statin1_chunk.py
	@cd statin1_chunks && make
	@python $(PYROP)/pyrop.py statin1_chunk.py build/statin1.bin

clean:
	@cd statin1_chunks && make clean
	@rm -rf build
