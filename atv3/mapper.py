#!/usr/bin/env python
import sys

# Read each line from stdin
for line in sys.stdin.readlines():
    # Get the words in each line
    words = line.strip().split(' ')
    

    # Second column  is the .htlm
    # was removed '/' and ' " " '
    for item in words:
    	if item.startswith('user='):
    		print(item.replace('user=<','').replace('>,',''))
    
