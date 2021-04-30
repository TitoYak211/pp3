import random
import math
import sys

# generate an array of random numbers 1 to n
def random_sequence(n):
    random.seed()
    arr = []

    for i in range(n):
        arr.append(random.randint(1, 10**12))

    return arr


def kk(arr):
    if len(arr) <= 2:
        return -1

    max1 = max(arr)
    index_max1 = arr.index(max1)
    arr[index_max1] = -1

    max2 = max(arr)
    index_max2 = arr.index(max2)
    arr[index_max2] = -1

    d = abs(max1 - max2)

    while max2 != 0 and max1 != 0:

        if max1 > max2:
            arr[index_max1] = d
            arr[index_max2] = 0
        else:
            arr[index_max1] = 0
            arr[index_max2] = d

    
        new_max1 = max(arr)
        index_new_max1 = arr.index(new_max1)
        arr[index_new_max1] = -1

        new_max2 = max(arr)
        index_new_max2 = arr.index(new_max2)
        arr[index_new_max2] = -1

        d = abs(new_max1 - new_max2)

    return d

def arrPartition(arr):
    lst = []

    for i in range(len(arr)):
        lst.append(random.choice(range(1, len(arr) + 1)))
    return lst


def arrRep(arr):
    lst2 = []
    for i in range(len(arr)):
        lst2.append(random.choice([-1, 1]))
    return lst2


def residue(arr, rep):

    arr2 = [0] * len(arr)

    for (i, rep) in enumerate(rep):
        arr2[rep - 1] += A[i]

    return abs(kk(arr2, 0))


def standard_to_partition(arr):
    partition = []
    for i in range(len(arr)):
        if arr[i] == -1:
            partition.append(2)
        else:
            partition.append(1)
    return arr


def stdR(arr1, arr2):
    lst = []
    for (i, j) in zip(arr1, arr2):
        lst.append(i * j)
        
    total = sum(lst)

    return abs(total)


def nbr(arr):
    while True:
        i = random.randint(0, len(P[:]) - 1)
        j = random.randint(0, len(P[:]) - 1)

        if arr[i] != j:
            arr[i] = j

            break

    return arr


def stdNbr(arr):
    i, j = random.sample(range(arr[:]), 2)

    arr[i] = -arr[i]

    if random.uniform(0, 1) < 0.5:
        arr[j] = -arr[j]

    return arr


def strings(str_):
    if str_ == 'x':
        arr_rep = arrPartition
        std_r = residue
        std_nbr = nbr
    elif str_ == 'y':
        arr_rep = arrRep
        std_r = stdR
        std_nbr = stdNbr
    else:
        raise ValueError("Invalid representation!!!")

    return arr_rep, std_r, std_nbr

# Repeated random: repeatedly generate random solutions to the problem, as determined by the representation.
def repeateRandom(arr, str_, max_iter):
    arr_rep, std_r, std_nbr = strings(str_)

    S = arr_rep(arr)

    for i in range(max_iter):
        S1 = arr_rep(arr)

        if std_r(arr, S1) < std_r(arr, S):
            S = S1

    return std_r(arr, S)


# Hill climbing: generate a random solution to the problem, and then attempt to improve it through moves to better neighbors
def hillClimbing(arr, str_, max_iter):
    arr_rep, std_r, std_nbr = strings(str_)

    S = arr_rep(arr)

    for i in range(max_iter):
        S1 = arr_rep(arr)

        if std_r(arr, S1) < std_r(arr, S):
            S = S1

    return std_r(arr, S)


# Simulated annealing: generate a random solution to the problem, and then attempt to improve it through moves to neighbors, that are not always better
def simulatedAnnealing(arr, max_iter, str_):
    arr_rep, std_r, std_nbr = strings(str_)

    S = arr_rep(arr)

    S11 = S[:]

    def T(iter_):
        return (10 ** 10) * (0.8 ** (i // 300))

    for i in range(max_iter):
        S1 = std_nbr(S)

        if std_r(arr, S1) < std_r(arr, S):
            S = S1
        elif random.uniform(0, 1) < math.exp(float(-(std_r(arr, S1) - std_r(arr, S))) / T(iter_)):
            solution_x = solution_z

        if std_r(arr, S) < std_r(arr, S11):
            S11 = S

    return std_r(arr, S11)