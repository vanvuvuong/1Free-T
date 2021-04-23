from datetime import datetime
# SIMPLE LOG FUNCTION
def log(mes, dt=None):
	"""Loging the message depending on the time:
		mes: message you want to assign
		dt: the time you assign. None is by default,
	It will return the current time if time hasn't been typed"""
	dt = dt or datetime.now()
	dt = str(dt)
	message = "{1}: {2}".format(mes, dt)
	with open ("log", "a+") as f:
		f.write (message)
	return None