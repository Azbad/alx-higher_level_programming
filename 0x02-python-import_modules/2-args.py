#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = len(argv) - 1
    if a < 1:
        print("{} arguments.".format(a))
    elif a == 1:
        print("{} argument:".format(a))
    else:
        print("{} arguments:".format(a))

    for i in range(a):
        print("{}: {:s}".format(i + 1, argv[i + 1]))
