#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char version[6] = "v0.1.0";

int main(int argc, char *argv[]) {
	printf("Welcome to UnitConv %s\n\n", version);
	
	char *usage = "Usage: %s -i <unit>=<value> -o <unit>[:<unit>:<unit>...]\n";
	
	// Option variables
	extern char *optarg;
	extern int optind;
	
	// Flags and values for arguments
	int hflag = 0;
	int iflag = 0;
	char *ivalue;
	int oflag = 0;
	char *ovalue;
	int err = 0;
	int c;
	
	// Read arguments
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
	
	// Identify '=' sign position
	int epos = 0;
	
	while(1) {
		if(ivalue[epos] == '=') {
			break;
		} else if(ivalue[epos] == '\0') {
			printf("Improper usage of arguments.\n");
			printf(usage, argv[0]);
			exit(1);
		}
		epos++;
	}
	
	free(usage);
	
	char unitin[epos];
	
	printf("%s\n", unitin);
	
	free(optarg);
	free(ivalue);
	free(ovalue);
	
	return 0;
}
