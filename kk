import partitions as Karp
import sys

if len(sys.argv) > 1:
    arr = []

    with open(sys.argv[1]) as file:
        for i in file:
            arr.append(int(i))

    file.close()

    print(Karp.kk(arr,0))