import multiprocessing


def run(data, map_func, reduce_func):
    with multiprocessing.Pool() as pool:

        d = {}
        for k, v in pool.imap(map_func, data):
            if d.get(k) is None:
                d[k] = []
            d[k].append(v)

        pool.map(reduce_func, d.items())
