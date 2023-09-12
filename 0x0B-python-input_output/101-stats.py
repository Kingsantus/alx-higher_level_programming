#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

file_size = 0
status_code_counts = {}

try:
    for i, line in enumerate(sys.stdin, 1):
        # Update file size
        file_size += int(line.split()[-1])

        # Update status code counts
        status_code = line.split()[8]
        status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

        # Print statistics every 10 lines
        if i % 10 == 0:
            print(f"Total file size: {file_size}")
            for code in sorted(status_code_counts):
                print(f"{code}: {status_code_counts[code]}")

except KeyboardInterrupt:
    # Print final statistics on keyboard interruption
    print(f"Total file size: {file_size}")
    for code in sorted(status_code_counts):
        print(f"{code}: {status_code_counts[code]}")
