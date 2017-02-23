export PYROP:="$(CURDIR)/pyrop"

all: letter.bin

letter.bin: rop/build
	@cd letter && make

rop/build:
	@cd rop && make

clean:
	@cd letter && make clean
	@cd rop && make clean
