#!/usr/bin/env python
import sys

# users dict, The keys are be user names, values are the occurences
# {'user1': 3, 'user2': 2}
users = {}

# Process each line from the mapper
for line in sys.stdin:
    # values are separated by \n
    name = line.split('\n')[0]

    # Search the name on the users dict
    if (name in users.keys()):
        # If the name is in the dict, add 1 ocurrence to it
        users[name] += 1
    else:
        # If the name is not in the dict, add it with 1 occurence
        users[name] = 1

# Transforms the dict in a list of tuples
users_list = users.items()

# Sort the list of users by their occurrences in reverse order
sorted_log = sorted(users_list, key=lambda tup: tup[1], reverse=True)

for user in sorted_log:
    if user[1] > 100:
        print('{0}\t{1}'.format(user[0], user[1]))
