#!/usr/bin/python


FILE = "files/26.txt"
ST = 1633305600
ET = ST + 7*86400


def main():
    with open(FILE, "r") as f:
        n = int(f.readline())
        count = 0
        pl = [0 for _ in range(7*86400)]
        for l in f.readlines():
            sp, ep = [int(x) for x in l.split()]
            if sp < ST and (ep > ST or ep == 0):
                count += 1
            if sp >= ST and sp <= ET:
                i = sp - ST - 1
                if i < 0:
                    i = 0
                pl[i] += 1
            if ep >= ST and ep <= ET:
                i = ep - ST - 1
                if i < 0:
                    i = 0
                pl[i] -= 1

        mp = 0
        st = 0
        for c in pl:
            count += c
            if count > mp:
                mp = count
                st = 0
            if count == mp:
                st += 1
    print(mp, st)


if __name__ == "__main__":
    main()
