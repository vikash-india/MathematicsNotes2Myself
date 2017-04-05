# Description: Inverse Element

from numpy.linalg import inv
from numpy import array

# Additive Inverse
print (-1 * 2)          # Returns -2. Additive inverse of 2.
print (-1 * 344)        # Returns -344. Additive inverse of 344.

# Multiplicative Inverse
a = array([[1.]])
print inv(a)            # Returns 1. Multiplicative inverse of 1.

a = array([[2.]])
print inv(a)            # Returns 0.50000. Multiplicative inverse of 2.

a = array([[3.]])
print inv(a)            # Returns 0.33333. Multiplicative inverse of 3.

# TODO
# - None
