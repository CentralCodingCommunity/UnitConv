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
version = "v0.1-alpha0"

# Input and output units
iunit = None
ounit = None


### HELP FUNCTIONS ###
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
# Convert area
def areaConv(arg):
	print "Area..."

# Convert distance
def distConv(arg):
	print "Distance..."

# Convert mass
def massConv(arg):
	print "Mass..."

# Convert temperature
def tempConv(arg):
	colonPos = arg.find(":", 2)
	if colonPos == -1:
		print "Incorrect usage."
		printUsage()
		sys.exit(2)
	iunit = arg[colonPos-1]
	ounit = arg[colonPos+1]

	if iunit == ounit:
		print "Nice joke, these units are the same."
		sys.exit(2)

	try:
		num = float(arg[:colonPos-1])
	except ValueError:
		print "You did not enter a number before the unit."
		sys.exit(2)
	
	if iunit == "C" and ounit == "F":
		print (num * (9.0/5.0)) + 32
	elif iunit == "C" and ounit == "K":
		print num - 273
	elif iunit == "F" and ounit == "C":
		print (num - 32) * (5.0/9.0)
	elif iunit == "F" and ounit == "K":
		print (num - 32) * (5.0/9.0) - 273
	elif iunit == "K" and ounit == "C":
		print num + 273
	elif iunit == "K" and ounit == "F":
		print ((num - 273) * (9.0/5.0)) + 32
	else:
		print "One or more of the units (", iunit, ",", ounit, ") entered is not valid.\nUse the -h or --help option for a list of valid units."
		sys.exit(2)

	sys.exit(0)

# Convert speed/velocity
def speedConv(arg):
	print "Speed..."

# Convert volume
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
