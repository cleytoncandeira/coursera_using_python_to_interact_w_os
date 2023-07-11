#!/usr/bin/env python3

import re

def rearrange_name(name):
	result = re.search(r"([\w .]*), ([\w .]*)$", name)
	
	if result is None:
		return name   #to edge 1 - "" (empty), to 2, name
		
	return "{} {}".format(result[2], result[1])
	
	
	
	




