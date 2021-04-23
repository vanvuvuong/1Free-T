# Closure can make python better performance than class
# def outer():
# 	# begin closure
# 	x = 'test'
# 	def inner ():
# 		nonlocal x 
# 		x += ' this'
# 		print (f'{x} test')
# 		#end closure
# 	return inner
# a = outer()
# a()

# CLOSURE APPLICATION
counter = {}
def count(fn):
	cnt = 0 # local variable of this scope
	def add(*args, **kwargs):
		nonlocal cnt
		cnt += 1
		# print (f"The {fn.__name__}")
		counter[fn.__name__] = cnt
		return fn(*args, **kwargs)
	return add

def adds (a,b):
	return a + b
	
counter_add = count(adds)
counter_add (1,2)
counter_add (3,2)
print (counter)