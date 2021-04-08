import math


def miller_test(n: int) -> bool:
    """
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    :param n:
    :return: whether n is prime
    """
    if n <= 1:
        return False
    if n % 2 == 0:
        return False
    # write n as 2^r d + 1
    r = 0
    while True:
        if (n - 1) % 2 ** r == 0:
            r += 1
            continue
        r -= 1
        break
    d = (n - 1) // 2 ** r
    # loop
    for a in range(2, 1 + min(n - 2, int(2 * math.log(n) ** 2))):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        passed = False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                passed = True
                break
        if not passed:
            return False
    return True
