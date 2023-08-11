#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    dirname = dir(hidden_4)
    for n in dirname:
        if n[:2] != "__":
            print("{}".format(n))
