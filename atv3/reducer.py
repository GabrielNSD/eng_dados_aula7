#!/usr/bin/env python
import sys

users = []

# Process each key-value pair from the mapper
for line in sys.stdin:
	# values are separated by \n
	log , x = line.split('\n')
	

	if(log in x[1] for x in users):
		x=5 #só pra testar 
		#index2 = users.index(log)
		#users[user][1] = 
		#users[index2][1] = users[index2][1] + 1

	else:
		entry_tuple = (log, 0)
		users.append(entry_tuple)

sorted_log = sorted(users, reverse=True)


for user in sorted_log:
	if user[1] > 100:
		print('{0}\t{1}'.format(users[0], users[1]))
	else:
		break

