def add(increment):
	def decorator(func):
		def wrapper (*args, **kwargs):
			return func(*args, **kwargs) + increment
		return wrapper
	return decorator

def multiply(multiplier):
	def decorator(func):
		def wrapper (*args, **kwargs):
			return func(*args, **kwargs) * multiplier
		return wrapper
	return decorator



@multiply(3)
def f(n):
	return n + 2

print f(4)