export PYROP:="$(CURDIR)/pyrop"

all: ropdb/DB.py code/build letter.bin

ropdb/DB.py:
	@cp ropdb/$(REGION).py ropdb/DB.py

code/build:
	@cd code && make

letter.bin: rop/build
	@cd letter && make

rop/build:
	@cd rop && make

clean:
	@rm ropdb/DB.py
	@cd letter && make clean
	@cd rop && make clean
	@cd code && make clean
