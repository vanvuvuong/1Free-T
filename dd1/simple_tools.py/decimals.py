import decimal
from decimal import Decimal
# SET CONTEXT
ctx = decimal.getcontext() # default context
local_ctx = decimal.localcontext() # default context

# SET PROPERTIES
ctx.precision = 30 # set the number of precision
ctx.rounding = 'ROUND_HALF_EVEN' # set the rounding mechanism, values in list: [ROUND_CEILING, ROUND_FLOOR, ROUND_UP, ROUND_DOWN,ROUND_HALF_UP, ROUND_HALF_DOWN, ROUND_HALF_EVEN, ROUND_05UP]

# MAKE GLOBAL
decimal.getcontext.rounding() = decimal.ROUND_HALF_DOWN
dec = Decimal(15) # decimal from int
dec = Decimal('15.3551') # decimal from string
dec = Decimal(1, (3,2,4,5,6), -3) # decimal from tuple - 1/0 in head is the sign, the last ("-3") is the exponent - "-32.456"

# MAKE LOCAL
with decimal.localcontext() as ctx:
	ctx.precision = 4
	ctx.rounding = decimal.ROUND_HALF_UP