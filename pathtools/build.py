#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

import common


template = "{prefix}{version}/{buildtype}{suffix}"
patterns = {
	"version"        : r"[0-9][0-9]\.[0-9][0-9]\.[0-9][0-9]",
	"buildtype"      : "|".join(common.valid_buildtypes),
}

def parse(path):
	return common.parse(path, template, patterns)

def compose(version, buildtype, prefix="", suffix=""):
	print(locals())
	return common.compose(template, **locals())

def check(parts):
	return common.check(patterns, **parts) 

def main():
	path = "Builds/06.49.02/debug/log.log"
	parts = parse(path)
	check(parts)
	print(compose(**parts))

if __name__ == "__main__":
	main()
