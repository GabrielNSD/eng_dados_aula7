#!/usr/bin/env python
import sys

# list of urls
url = []
# Process each key-value pair from the mapper
for line in sys.stdin:
    # values are separated by \t
    url_aux2 = line.strip().split('.')

    # If the name of file is equal or less than 5 characters, appends it to the list
    if len(url_aux2[0]) <= 5:
        url_aux = line
        url.append(line)

for site in url:

    print('{0}'.format(site).replace("[", "").replace("]", "").replace(
        "'", "").replace("'", "").replace("\n", ""))
