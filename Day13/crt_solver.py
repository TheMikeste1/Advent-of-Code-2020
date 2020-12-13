def egcd(a: int, b: int) -> tuple:
    """
    Calculates the Greatest Common Denominator for the
    given a and b using Bézout's identity:
        ax + by = gcd(a, b)

    When a and b are coprime (gcd = 1), x will be a (mod b)'s inverse
    and y will be b (mod a)'s inverse.
    """
    # if 0 is the b, the answer will always be the same
    if b == 0:
        #    a * 1 + num * b = a = gcd
        #    gcd,  x,  y (could be anything, but 0 works)
        return a,   1, 0

    q = a // b  # Get how many times b goes into a
    r = a % b   # Get the remainder after dividing

    # Get the x and y from the next level
    gcd, sub_x, sub_y = egcd(b, r)

    # y = (gcd - ax) / b
    # y = gcd / b - qx
    #    sub_x ~= gcb / b  TODO: ???
    # y = sub_x - qx
    #    x = sub_y         TODO: ???
    y = sub_x - q * sub_y

    #      gcd,     x, y
    return gcd, sub_y, y


def find_TUMMI(val, mod):
    """
    TUMMI = The Unique Modular Multiplicative Inverse.

    This is the smallest positive number a value can be
    multiplied by so val % mod = 1.

    NOTE: val and mod _must_ be coprime!
    """
    # Putting the smaller value second results in one less
    # iteration of egcd. Whereas val is likely the smaller
    # unit, we will place it second.
    gcd, mod_inverse, inverse = egcd(mod, val)
    if gcd != 1:
        raise ArithmeticError(f"{val} and {mod} are not coprime! GCD: {gcd}")
    return inverse % mod


def crt_solver(*vals):
    """
    Chinese Remainder Theorem

    Takes in a number of pairs in form (divisor, remainder),
    and returns the lowest simultaneous solution.

    :param vals: Pairs in form (divisor, remainder)
    :return: The lowest valid number that satisfies all remainders for each divisor
    """
    product = 1
    for num, _ in vals:
        product *= num

    x = 0
    for num, remainder in vals:
        o = product // num
        y = find_TUMMI(o, num)
        x += remainder * o * y

    x = x % product
    return x
