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
print_all(a=1)