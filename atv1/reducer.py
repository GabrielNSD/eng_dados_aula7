#!/usr/bin/env python
import sys

salaries = []
# Process each key-value pair from the mapper
for line in sys.stdin:
    # values are separated by \t
    name, salary = line.split('\t')

    # converts salary to float
    salary = float(salary)

    # the pair salary&name is stored as a tuple, with salary as first item since it has priority on sorted() comparision
    entry_tuple = (salary, name)
    # each pair is appended to the list
    salaries.append(entry_tuple)

# sort the list in descending order
sorted_salaries = sorted(salaries, reverse=True)

# print 10 first salaries
for pair in sorted_salaries[:10]:
    print('{0}\t{1}'.format(pair[1], pair[0]))