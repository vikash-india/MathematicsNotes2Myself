# Description: Rational Numbers

# Convert Fractions to Rational Numbers
[n, d] = rat(.75)           # n=3, d=4.
[n, d] = rat(pi)            # n=355, d=113. Converts a non-recurring non-terminating fraction.
[n, d] = rat(4/6)           # n=2, d=3. Returns the rational number to lowest term.

# Convert Rational Numbers to Fractions
3/4                         # 0.75000.
355/113                     # 3.1416.
4/6                         # 0.66667.

# TODO
# - None
