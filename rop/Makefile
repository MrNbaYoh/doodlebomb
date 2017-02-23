all: rop_stage1 rop_stage0

rop_stage0: rop_stage0.py
	@python $(PYROP)/pyrop.py rop_stage0.py build/rop_stage0.bin

rop_stage1: rop_stage1.py
	@python $(PYROP)/pyrop.py rop_stage1.py build/rop_stage1.bin

clean:
	@rm -rf build
