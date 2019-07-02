# Description: Factors of a Number

# Prime Factors of a Number
factor(2310)                                            # 2 3 5 7 11. Returns all prime factors of a number.
factor(32)                                              # 2 2 2 2 2. Returns all prime factors of a number.

# All Factors of a Number
number=8; i=1:number; factors = i(rem(number, i) == 0)  # 1 2 4 8. Returns all factors of a number.
D=[1; unique(cumprod(perms(factor(N)),2))]              # 1 2 4 8. Same as above but faster for large numbers.

# TODO
# - None
