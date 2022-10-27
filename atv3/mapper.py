#!/usr/bin/env python
import sys

# Read each line from stdin
for line in sys.stdin.readlines():
    # Get the words in each line
    words = line.strip().split(' ')

    # Print the username fo each login attempt
    for item in words:
        if item.startswith('user='):
            print(item.replace('user=<', '').replace('>,', ''))
