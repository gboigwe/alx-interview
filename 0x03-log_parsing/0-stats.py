#!/usr/bin/python3
"""
Parsing a log and printing stats to stdout
All done by Module
"""


from sys import stdin

d_status_code = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

size = 0


def print_stats():
    """Accumulated logs is being printed"""
    print("File size: {}".format(size))
    for status in sorted(d_status_code.keys()):
        if d_status_code[status]:
            print("{}: {}".format(status, d_status_code[status]))


if __name__ == "__main__":
    count = 0
    try:
        for line in stdin:
            try:
                items = line.split()
                size += int(items[-1])
                if items[-2] in d_status_code:
                    d_status_code[items[-2]] += 1
            except:
                pass
            if count == 9:
                print_stats()
                count = -1
            count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
