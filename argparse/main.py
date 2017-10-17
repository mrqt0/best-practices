#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
print_help():
- usage
- description
- argument groups
- epilog

error:
- usage
- error msg
- exit

"""

import argparse
import collections
import sys

class Build():
	def __init__(self):
		print("Build")
		pass

class Test():
	def __init__(self, argv, parser):
		print("Test")
		self.parser = parser
		self.parse_args(argv)

	def parse_args(self, argv):
		self.parser.add_argument("--campaign")
		self.args = self.parser.parse_args(argv)
		print(self.args)

	def check_args(self):
		pass

modules = collections.OrderedDict()
modules["build"] = "Build"
modules["test"] = "Test"

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("module", type=type_module)
	args = parser.parse_args(sys.argv[1:2])

	module_parser = argparse.ArgumentParser(prog="{} {}".format(sys.argv[0], sys.argv[1]))
	module_parser.add_argument("--loglevel")

	class_instance = args.module(sys.argv[2:], module_parser)
	class_instance.run()

def type_module(string):
	if string not in modules.keys():
		raise argparse.ArgumentTypeError("Error")
	classname = modules[string]
	module = globals()[classname]
	return module

#def type_campaign(string):
#	pass



if __name__ == "__main__":
	main()
