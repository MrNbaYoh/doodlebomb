all: statin1_chunk common1 dstinf1 rcvinf1 miistd1 colslt1 sheet1

sheet1: sheet1.py
	@python $(PYROP)/pyrop.py sheet1.py build/sheet1.bin

common1: common1.py
	@python $(PYROP)/pyrop.py common1.py build/common1.bin

dstinf1: dstinf1.py
	@python $(PYROP)/pyrop.py dstinf1.py build/dstinf1.bin

rcvinf1: rcvinf1.py
	@python $(PYROP)/pyrop.py rcvinf1.py build/rcvinf1.bin

colslt1: colslt1.py
	@python $(PYROP)/pyrop.py colslt1.py build/colslt1.bin

miistd1: miistd1.py
	@python $(PYROP)/pyrop.py miistd1.py build/miistd1.bin

statin1_chunk: statin1.py
	@cd statin1_chunks && make
	@python $(PYROP)/pyrop.py statin1.py build/statin1.bin

clean:
	@cd statin1_chunks && make clean
	@rm -rf build
