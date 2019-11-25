#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
parser.print_help():
- usage # 
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
		self.parser = get_parser()
		self.parser.print_help()
		self.parser.print_usage()
		pass

	def run(self):
		pass

class Test():
	def __init__(self):
		print("Test")
		self.parser = get_parser()
		self.parse_args()

	def parse_args(self):
		self.parser.add_argument("--campaign")
		self.args = self.parser.parse_args(sys.argv)

	def check_args(self):
		pass

	def run():
		pass

modules = collections.OrderedDict()
modules["build"] = "Build"
modules["test"] = "Test"

def type_module(string):
	if string not in modules.keys():
		raise argparse.ArgumentTypeError("Error")
	classname = modules[string]
	module = globals()[classname]
	return module

def get_parser():
	module_parser = argparse.ArgumentParser(prog="{} {}".format(sys.argv[0], sys.argv[1]))
	module_parser.add_argument("module", help=argparse.SUPPRESS)
	module_parser.add_argument("--loglevel")
	return module_parser

def main():
	print(sys.version)
	parser = argparse.ArgumentParser()
	parser.add_argument("module", type=type_module)
	args = parser.parse_args(sys.argv[1:2])

	class_instance = args.module()
	class_instance.run()

if __name__ == "__main__":
	main()
