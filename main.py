import time

from apr_cl import apr_test
from primality_test import miller_test


def timeit(f, *args, **kwargs):
    t1 = time.time()
    f(*args, **kwargs)
    t2 = time.time()
    print(f"elapsed time: {t2 - t1}")


if __name__ == "__main__":
    n = 2 ** 521 - 1
    print("apr_test")
    timeit(apr_test, n)
    print("miller_test")
    timeit(miller_test, n)
