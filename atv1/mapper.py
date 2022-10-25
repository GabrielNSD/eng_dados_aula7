#!/usr/bin/env python
import sys

# Read each line from stdin
for line in sys.stdin.readlines():
    # Get the words in each line
    words = line.split(",")

    # All the names are sepparated by comma, so the first two items correspond to a name,
    # The column before the last(?) corresponds to the salary
    print('{0}, {1}\t{2}'.format(words[0].replace('"', ""),
                                 words[1].replace('"', ""),
                                 words[-2]).replace('$', ""))
