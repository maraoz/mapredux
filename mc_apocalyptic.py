import time

import mapredux


def map_func(n):
    b = 2**n
    is_apocalyptic = '666' in str(b)
    return (is_apocalyptic, n)


def reduce_func(item):
    boolean, numbers = item
    if not boolean:
        return
    print("apocalyptic:", numbers)


def find_apocalyptic(S, E):
    r = range(S, E)

    mapredux.run(r, map_func, reduce_func)


if __name__ == "__main__":
    start_time = time.time()
    find_apocalyptic(100, 1000)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
