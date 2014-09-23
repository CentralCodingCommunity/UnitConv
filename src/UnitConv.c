#include <stdio.h>
#include <stdlib.h>

char *version = "v0.1";

int main(int argc, char *argv[]) {
	printf("Welcome to UnitConv %s\n\n", version);
	
	char *usage = "Usage: %s -i <unit>=<value> -o <unit>[:<unit>:<unit>...]\n";
	
	extern char *optarg;
	extern int optind;
	
	int hflag = 0;
	int iflag = 0;
	char *ivalue;
	int oflag = 0;
	char *ovalue;
	int err = 0;
	int c;
	
	while((c = getopt(argc, argv, "hi:o:")) != -1) {
		switch(c) {
			case 'h':
				hflag = 1;
				break;
			case 'i':
				iflag = 1;
				ivalue = optarg;
				break;
			case 'o':
				oflag = 1;
				ovalue = optarg;
				break;
			case '?':
				err = 1;
				break;
		}
	}
	if(hflag == 1 && iflag == oflag == err == 0) {
		printf(usage, argv[0]);
		exit(0);
	} else if(iflag == 0 || oflag == 0 || err == 1) {
		printf("Improper usage of arguements.\n");
		printf(usage, argv[0]);
		exit(1);
	}
	
	printf("Input: %i\n", iflag);
	printf("Input Value: %s\n", ivalue);
	printf("Output: %i\n", oflag);
	printf("Output Value: %s\n", ovalue);
	
	return 0;
}
