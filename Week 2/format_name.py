# Complete the body of the format_name function. This function receives the first_name
# and last_name parameters and then returns a properly formatted string.

def format_name(first_name, last_name):
	# code goes here
	if first_name != '' and last_name != '':
		return "Name: " + last_name + ", " + first_name
	elif first_name != '' or last_name != '':
		return "Name: " + last_name + first_name
	else:
		return ''

print(format_name("Ernest", "Hemingway"))
print(format_name("", "Madonna"))
print(format_name("Voltaire", ""))
print(format_name("", ""))


