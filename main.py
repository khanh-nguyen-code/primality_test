import time
from typing import Any

from apr_cl import apr_test
from miller_test import miller_test


def timeit(f, *args, **kwargs) -> Any:
    t1 = time.time()
    out = f(*args, **kwargs)
    t2 = time.time()
    print(f"elapsed time: {t2 - t1}")
    return out


if __name__ == "__main__":
    for p in [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457]:
        n = 2 ** p - 1
        print(f"n = 2**{p} - 1 = {n}")
        print("apr_test", end="\t")
        if not timeit(apr_test, n):
            print("error")
        print("miller_test", end="\t")
        if not timeit(miller_test, n):
            print("error")
        print()
