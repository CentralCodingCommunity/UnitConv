SOURCEDIR=src
MAINFILE=$(SOURCEDIR)/UnitConv.c
BUILDDIR=bin
BINFILE=$(BUILDDIR)/unitconv

all:
	mkdir -p $(BUILDDIR)
	gcc $(MAINFILE) -o $(BINFILE)

clean:
	rm -rf $(BUILDDIR)
