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

version = "v0.1"

def printUsage():
	print "Usage:", sys.argv[0], "[option] [<measure_argument> <input><input_unit>:<output_unit>]"

def printHelp():
	printUsage()
	print """Still working on this bit."""

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "ht:v", ["help", "temp=", "version"])
	except getopt.GetoptError:
		printUsage()
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			printHelp()
			sys.exit(0)
		elif opt in ("-v", "--version"):
			print "UnitConv", version
			sys.exit(0)
		elif opt in ("-v", "--temp"):
			print "You chose temparature!!!"

if __name__ == "__main__":
	main(sys.argv[1:])
