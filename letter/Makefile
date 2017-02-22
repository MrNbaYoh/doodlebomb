all: letter

letter: letter.py
	@echo $(PYROP)
	@cd letter_chunks && make
	@python $(PYROP)/pyrop.py letter.py build/letter.bin

clean:
	@cd letter_chunks && make clean
	@rm -rf build
