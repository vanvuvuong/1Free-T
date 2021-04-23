# ALL THE THING IN PYTHON IS MEMORY REFERENCE


def func():
    print('Definition')


func()

# WHAT THE PYTHON ACTUALLY DO ?
# IT CREATES A FUNCTION OBJECT AND REFER TO func
# EXECUTE THE FUNCTION


# FUNCTION VARIABLES & PARAMETERS
def func(a, # param with default values must come later 
	b=1, c=2):
	sum = a+b+c
	print (sum)
    return sum

def func(a, b, *c):
	pass
func (1,2,3,4)
