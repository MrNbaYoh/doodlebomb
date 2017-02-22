all: stbard1 stahed1

stbard1: stbard1.py
	@python $(PYROP)/pyrop.py stbard1.py build/stbard1.bin

stahed1: stahed1.py
	@python $(PYROP)/pyrop.py stahed1.py build/stahed1.bin

clean:
	@rm -rf build
