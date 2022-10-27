#!/usr/bin/env python
import sys

# Read each line from stdin
for line in sys.stdin.readlines():
    # Get the words in each line, separated by \t
    words = line.strip().split("\t")

    # Second column  is the .htlm
    # was removed '/' and ' " " '
    print('{0}'.format(words[1].replace('/', "").replace('"', "")))
