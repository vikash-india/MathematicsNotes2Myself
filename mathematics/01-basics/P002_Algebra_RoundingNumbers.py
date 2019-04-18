# Description: Rounding Numbers

import numpy

# Round Up
numpy.ceil(1.2)             # Returns 2.0
numpy.ceil(1.9)             # Returns 2.0
numpy.ceil(-1.2)            # Returns -1.0

# Round Down
numpy.floor(1.9)            # Returns 1.0
numpy.floor(-1.9)           # Returns -2.0

# Truncate
numpy.trunc(1.23)           # Returns 1.0
numpy.trunc(1.51)           # Returns 1.0
numpy.trunc(-1.99)          # Returns -1.0

# Round
numpy.round(1.23)           # Returns 1.0
numpy.round(1.50)           # Returns 2.0
numpy.round(1.51)           # Returns 2.0

numpy.round(-1.23)          # Returns -1.0
numpy.round(-1.50)          # Returns -2.0
numpy.round(-1.51)          # Returns -2.0

# TODO
# - None
