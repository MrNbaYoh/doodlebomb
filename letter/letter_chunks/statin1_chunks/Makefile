all: stmask1 stahed1

stmask1: stmask1.py
	@python $(PYROP)/pyrop.py stmask1.py build/stmask1.bin

stahed1: stahed1.py
	@python $(PYROP)/pyrop.py stahed1.py build/stahed1.bin

clean:
	@rm -rf build
