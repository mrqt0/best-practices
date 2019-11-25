#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

valid_buildtypes = ("release", "debug")

def parse(path, template, patterns):
	e = _make_format_spec(formats)
	r = re.compile(template.format(**e))
	f = r.match(path)
	return f.groupdict()

def compose(template, **parts):
	return template.format(**parts)

def check(formats, **parts):
	for name, regex in formats.items():
		if name not in parts:
			raise Exception("Missing field {}".format(name))
		if not re.match(regex, parts[name]):
			raise Exception("Not formatted correctly: {}".format(parts[name]))

def _make_format_spec(d):
	e = dict()
	for key, val in d.items():
		e[key] = "(?P<{}>{})".format(key, val)
	return e
