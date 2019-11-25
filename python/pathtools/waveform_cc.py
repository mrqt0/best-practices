#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

import common


template = "{prefix}sr{system_release}/{waveform}/wf/{version}/{id}/{target}-{buildtype}-{encryption}{suffix}"
patterns = {
	"prefix"         : "(.*/)?",
	"suffix" 		 : "(/.*)?",
	"system_release" : "[0-9].[0-9]",
	"waveform"       : ".*",
	"version"        : r"[0-9][0-9]\.[0-9][0-9]\.[0-9][0-9]",
	"id"             : ".*",
	"target"         : "|".join(common.valid_targets),
	"buildtype"      : "|".join(common.valid_buildtypes),
	"encryption"     : r"\w*",
}

def parse(path):
	return common.parse(path, template, patterns)

def compose(system_release, waveform, version, id, target, buildtype, encryption, prefix="", suffix=""):
	print(locals())
	return common.compose(template, **locals())

def check(parts):
	return common.check(patterns, **parts) 

def main():
	path = "20_Waveform_Builds/sr6.5/hdr_aj_wb/wf/06.49.02/abcdef/sdtr-debug-development/meta/info.json"
	parts = parse(path)
	check(parts)
	print(compose(**parts))

if __name__ == "__main__":
	main()
