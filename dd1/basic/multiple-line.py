# For normal coding, python has physical line
# A physicaline has seperate with the "break line token"
# Sometimes for coding, physical lines are ignored
# and we need Logical Line.

# 1 Logical line can include multiple physical lines.
# like this one

a,b,c = '','','s'
if a \
	b and c:
	print ('This is a test')

# Implicit & Explicit:

### Implicit:
# like
def implicit (a, # you can make a command here
				b,c):
	pass

a = {
	1 : '1'
}	

# ....

### Explicit:
# like
a,b,c = '','','s'
if a \ #But you can't make a command here
	b and c:
	print ('This is a test')