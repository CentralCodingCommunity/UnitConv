SOURCEDIR=src
BUILDDIR=bin

all:
	mkdir -p $(BUILDDIR)
	gcc $(SOURCEDIR)/UnitConv.c -o $(BUILDDIR)/unitconv

clean:
	rm -rf $(BUILDDIR)
