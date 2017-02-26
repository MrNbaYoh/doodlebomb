all: rop_stage0 rop_stage1

rop_stage0: rop_stage0_base.py rop_stage0_final.py
	@python $(PYROP)/pyrop.py rop_stage0_base.py build/rop_stage0_base.bin
	@python $(PYROP)/pyrop.py rop_stage0_final.py build/rop_stage0.bin

rop_stage1: build/rop_stage0_base.bin rop_stage1.py
	@python $(PYROP)/pyrop.py rop_stage1.py build/rop_stage1.bin

clean:
	@rm -rf build
