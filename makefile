SOURCEDIR=src
BUILDDIR=bin
BINFILE=unitconv

all:
	mkdir -p $(BUILDDIR)
	gcc $(SOURCEDIR)/UnitConv.c -o $(BUILDDIR)/$(BINFILE)

clean:
	rm -rf $(BUILDDIR)
