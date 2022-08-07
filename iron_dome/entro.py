#!/usr/bin/env python3

import math

filename = "/home/rikrdo/github/cybersec/iron_dome/logs/jpg.jpg.ft"

with open(filename, "rb") as file:
    counters = {byte: 0 for byte in range(2 ** 8)}  # start all counters with zeros

    for byte in file.read():  # read in chunks for large files
        counters[byte] += 1  # increase counter for specified byte

    filesize = file.tell()  # we can get file size by reading current position

    probabilities = [counter / filesize for counter in counters.values()]  # calculate probabilities for each byte

    entropy = -sum(probability * math.log2(probability) for probability in probabilities if probability > 0)  # final sum

    print(entropy)