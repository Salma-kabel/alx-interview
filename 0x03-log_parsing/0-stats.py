#!/usr/bin/python3
""" Script that reads stdin line by line """


import sys


def print_stats(stats: dict, filesize: int) -> None:
    """print stats of files"""
    print("File size: {:d}".format(filesize))
    for key, value in sorted(stats.items()):
        if value:
            print("{}: {}".format(key, value))


def processinput():
    """parse stdin line by line and computes metrics"""
    filesize, count = 0, 0
    code = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {key: 0 for key in code}

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                statuscode = data[-2]
                if statuscode in stats:
                    stats[statuscode] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                pstats(stats, filesize)
        pstats(stats, filesize)
    except KeyboardInterrupt:
        pstats(stats, filesize)
        raise


if __name__ == "__main__":
    processinput()
