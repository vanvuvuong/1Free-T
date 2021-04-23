# Each time you try to assign a variable
# it is memory reference.
# For this you can take care the address of
# Memory to know what exactly an variable is
a = 4
print(id(a))
print(hex(a))

# References
# You can count the reference of a
# variable in with these

# 1st way
import ctypes
def ref_count(address):
    return ctypes.c_long.from_address(address).value

print(ref_count(a))

# 2nd way
import sys

print(sys.getrefcount(a))