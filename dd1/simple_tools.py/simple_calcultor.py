import decimal
from decimal import Decimal

# SET THE LOCAL ONLY PRECISION & ROUNDING MECHANISM
def to_decimal(element1 = '', element2 = '',base = 'STRING_BASED', **kwargs):
	'''Calculate the decimal calculation with the multiple base type of element.
	Such as [STRING_BASED, TUPLE_BASED, INT_BASED]'''
	
	# String base decimals
	if base == 'STRING_BASED':
		with decimal.localcontext() as ctx:
			ctx.precision = 4
			ctx.rouding = decimal.ROUND_HALF_UP
			dec1 = Decimal(element1)
			dec2 = Decimal(element2)
			return dec1, dec2
	if base == 'TUPLE_BASED':
		with decimal.localcontext() as ctx:
			ctx.precision = 4
			ctx.rouding = decimal.ROUND_HALF_UP
			dec1 = Decimal(element1)
			dec2 = Decimal(element2)
		

# SET to_decimal PROPERTIES
to_decimal.STRING_BASE = 'STRING_BASE'
to_decimal.TUPLE_BASED = 'TUPLE_BASED'
to_decimal.INT_BASED = 'INT_BASED'