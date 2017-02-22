export PYROP:="$(CURDIR)/pyrop"

all:
	@cd letter && make

clean:
	@cd letter && make clean
