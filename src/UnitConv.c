/**
 * COPYRIGHT (C) 2014 Nicolás A. Ortega
 * 
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * 
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char version[6] = "v0.1";

int main(int argc, char *argv[]) {
	printf("Welcome to UnitConv %s\n\n", version);
	
	char usage[100] = "Usage: %s -i <unit>=<value> -o <unit>[:<unit>:<unit>...]\n";
	
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
	
	char unitin[100];
	memcpy(unitin, ivalue, epos);
	
	printf("%s\n", unitin);
	
	/*int ovalsize = 0;
	while(1) {
		if(ovalue[ovalsize] == '\0') {
			break;
		}
		ovalsize++;
	}
	
	char tmpoutarg[ovalsize] = ovalue;*/
	
	return 0;
}
