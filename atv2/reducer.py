#!/usr/bin/env python
import sys

url = []
# Process each key-value pair from the mapper
for line in sys.stdin:
    # values are separated by \t
    url_aux2 = line.strip().split('.')

    if len(url_aux2[0]) <= 5:
        url_aux = line.split('\t')
        #url_aux = url_aux.split('\n')
        url.append(url_aux)

# sort the list in descending order
#sorted_salaries = sorted(salaries, reverse=True)

# print 10 first salaries
for site in url:

    print('{0}'.format(site).replace("[", "").replace("]", "").replace(
        "'", "").replace("'", "").replace("\n", ""))
