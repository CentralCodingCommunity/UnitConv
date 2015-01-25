##
# UnitConv, a commandline unit converter.
# Copyright (C) 2014  Nicolas A. Ortega
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
import getopt, sys

# Version tag
version = "v0.1"

# What measurement are we converting in
measurement = ""

# Input and output units
iunit = ""
ounit = ""

### PREDEFINED FUNCTIONS ###
def printUsage():
	print "Usage:", sys.argv[0], "[option] | [<measurement> <input><input_unit>:<output_unit>]"

def printHelp():
	printUsage()
	print """
Measurements and Units:
	-a or --area		-- Area
	-d or --dist		-- Distance
	-m or --mass		-- Mass
	-t or --temp		-- Temperature
		C		-- Celsius
		F		-- Fahrenheit
		K		-- Kelvin
	-s or --speed		-- Speed
	-v or --vol		-- Volume

Other Arguments:
	-h or --help		-- Print this help information.
	--version		-- Print the version of UnitConv installed.

Example:
	""", sys.argv[0], """ --temp 32F:C"""

### CONVERSION FUNCTIONS ###
def areaConv(arg):
	print "Area..."

def distConv(arg):
	print "Distance..."

def massConv(arg):
	print "Mass..."

def tempConv(arg):
	print "You chose temperature with argument", arg

def speedConv(arg):
	print "Speed..."

def volConv(arg):
	print "Volume..."

### MAIN FUNCTION ###
def main(argv):
	try:
		opts, args = getopt.getopt(argv, "a:d:m:ht:s:v:", ["area=", "dist=", "help", "mass=", "temp=", "speed=", "version"])
	except getopt.GetoptError:
		printUsage()
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			printHelp()
		elif opt == "--version":
			print "UnitConv", version
		elif opt in ("-a", "--area"):
			areaConv(arg)
		elif opt in ("-d", "--dist"):
			distConv(arg)
		elif opt in ("-m", "--mass"):
			massConv(arg)
		elif opt in ("-t", "--temp"):
			tempConv(arg)
		elif opt in ("-s", "--speed"):
			speedConv(arg)
		elif opt in ("-v", "--vol"):
			volConv(arg)

		sys.exit(0)

### CALL MAIN FUNCTION ###
if __name__ == "__main__":
	main(sys.argv[1:])
