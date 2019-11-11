# 7.10 Dream Vacation

#Prompt: Write a program that polls users about their dream vacation. Write a prompt similar to "If you could visit one place in the world,
#where would you go?" Include a block of code that prints the results of the poll.

# build flag (for fun) and dictionary
flag = True
poll_data = {}
print()
while flag == True:
	# take down names, dream destinations, and will to continue
	poll_name = input('Enter your name: ')
	poll_place = input('Enter your dream destination: ')
	poll_continue = input('Continue the poll? (yes/no) ')
	# do not take down names or places if they mean to quit
	if poll_name == 'quit' or poll_place == 'quit':
		break
	# enter in new data, and do not continue if not desired.
	else:
		poll_data[poll_name] = poll_place
		if poll_continue == 'no':
			flag = False
print('Our survey says that:')
for name, place in poll_data.items():
	print(name + ' wants to go to ' + place + '! That is expensive but achievable!')
