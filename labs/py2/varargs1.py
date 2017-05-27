def print_args(*args):
	for arg in args:
		print(arg)

def print_all(*args, **kwargs):
	for arg in args:
		print arg
	for key, value in kwargs.items():
		print "Key: {}, Value: {}".format(key, value)

print_args("red", "blue", "green")
# print_args(1, ["1", "2"], (1,2,3), {'key': 'value'})

# calling this with a keyword argument will trigget an error
# print_args(a=1)

# however, the print_all function takes care of that
print_all(a=1)