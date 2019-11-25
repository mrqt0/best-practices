#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

valid_targets = ("sdtr", "sdar", "sdhr")
valid_buildtypes = ("release", "debug")
valid_encryptions = ("development", "internal", "production")

class PathTools():
	template = None
	formats = None

	def parse(self, path):
		e = self.make_format_spec(self.formats)
		r = re.compile(self.template.format(**e))
		f = r.match(path)
		return f.groupdict()

	def check(path):
		pass

	def make_format_spec(self, d):
		e = dict()
		for key, val in d.items():
			e[key] = "(?P<{}>{})".format(key, val)
		return e

class WaveformPath(PathTools):
	template = "{prefix}sr{system_release}/{waveform}/wf/{version}/{id}/{target}-{buildtype}-{encryption}{suffix}"
	formats = {
		"prefix"         : "(.*/)?",
		"suffix" 		 : "(/.*)?",
		"system_release" : "[0-9]\\.[0-9]",
		"waveform"       : ".*",
		"version"        : r"[0-9][0-9]\.[0-9][0-9]\.[0-9][0-9]",
		"id"             : ".*",
		"target"         : "|".join(valid_targets),
		"buildtype"      : "|".join(valid_buildtypes),
		"encryption"     : r"\w*",
	}




def main():
	path = "20_Waveform_Builds/sr6.5/hdr_aj_wb/wf/06.49.02/abcdef/sdtr-debug-development/meta/info.json"
	print(WaveformPath().parse(path))

if __name__ == "__main__":
	main()
