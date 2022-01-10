# Yussef Ibarra
# Programming Assignment 1 - Algorithms

"""
This program takes an integer n>=0 to generate an array of size n. This
generated array has positive integers in randomized order. The program returns
the runtime for the following sorting algorithms: insertion sort, merge sort,
heap sort, quicksort, randomized quicksort, and radix sort LSD.
"""

# Required for a random generator
import random
# Required for tracking time of runtime
import time


# Precondition: input is a positive integer or 0
# Postcondition: returns an array of positive integers in random order;
# array size is the input
def generateArray(size):
    return [random.randint(1, size) for n in range(size)]


# InsertionSort

# Precondition: Array A of numbers of size n
# Postcondition: Array A is sorted
def insertionSort(A, n):
    for j in range(1, n):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key


# MergeSort

# Precondition: Array A of numbers,
# lower bound index 'left';upper bound index 'right';middle index 'mid'
# Postcondition: Array A is sorted
def merge(A, left, right, mid):
    L = A[left:mid + 1]
    R = A[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    # Merging step
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
        k = k + 1

    # Place any remaing numbers from the merging step
    while i < len(L):
        A[k] = L[i]
        i = i + 1
        k = k + 1

    while j < len(R):
        A[k] = R[j]
        j = j + 1
        k = k + 1


# Precondition: Array A of numbers;
# lower bound index 'left';upper bound index 'right'
# Postcondition: Array A is sorted
def mergeSort(A, left, right):
    # Base case if left = right
    if left < right:
        mid = (left + right) // 2
        # Dividing step
        mergeSort(A, left, mid)
        mergeSort(A, mid + 1, right)
        # Conquering step
        merge(A, left, right, mid)


# HeapSort

# Precondition: Array A of numbers; Array size of n;
# i is subtree's root node
# Postcondition: Array A is reaaranged to satisfy heap properties
def heapify(A, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and A[i] < A[l]:
        largest = l

    if r < n and A[largest] < A[r]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, n, largest)


# Precondition: Array A of numbers; Array size of n
# Postcondition: Array A is reaaranged to satisfy heap properties
def buildHeap(A, n):
    for i in range(n, -1, -1):
        heapify(A, n, i)


# Precondition: Array A of numbers
# Postcondition:  Array A is sorted
def heapSort(A):
    n = len(A)
    # Array A is rearranged to satisfy heap properties
    buildHeap(A, n)
    # Extract the heap's root (largest number), place at the end of array
    # Size of heap decreases by 1 each iteration
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)


# Quicksort

# Precondition: Array A of numbers; lower bound index 'p'
# upper bound index 'r'
# Postcondition: Return index of pivot; All values left to the pivot
# are less than or equal to the pivot; All values right to the pivot are
# greater than the pivot
def partition(A, p, r):
    # Pivot is last element in A
    x = A[r]
    i = (p - 1)
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return (i + 1)


# Precondition: Array A of numbers; lower bound index 'p'
# upper bound index 'r'
# Postcondition: Array A is sorted
def quickSort(A, p, r):
    # Base case if p = r
    if (p < r):
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)


# QuicksortRandom

# Precondition: Array A of numbers; lower bound index 'p'
# upper bound index 'r'
# Postcondition: Return index of pivot; All values left to the pivot
# are less than or equal to the pivot; All values right to the pivot are
# greater than the pivot
def partitionR(A, p, r):
    # Pivot is a random element in A
    rand = random.randrange(p, r)
    # Switch chosen pivot with last element in A
    A[r], A[rand] = A[rand], A[r]
    x = A[r]
    i = (p - 1)
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return (i + 1)


# Precondition: Array A of numbers; lower bound index 'p'
# upper bound index 'r'
# Postcondition: Return sorted array
def quickSortR(A, p, r):
    # Base case if p = r
    if (p < r):
        q = partitionR(A, p, r)
        quickSortR(A, p, q - 1)
        quickSortR(A, q + 1, r)


# RadixSortLSD
# Precondition: Array A of numbers, int exp
# Postcondition: The least significant digits given by exp are sorted
def countingSort(A, exp):
    n = len(A)
    B = [0] * (n)
    C = [0] * (10)
    for i in range(0, n):
        index = (A[i] / exp)
        C[int(index % 10)] += 1
    for i in range(1, 10):
        C[i] = C[i] + C[i - 1]
    i = n - 1
    while i >= 0:
        index = (A[i] / exp)
        B[C[int((A[i] / exp) % 10)] - 1] = A[i]
        C[int((A[i] / exp) % 10)] -= 1
        i -= 1
    i = 0
    for i in range(0, len(A)):
        A[i] = B[i]


# Precondition: Array A of numbers
# Postdition: Array A is sorted
def radixSort(A):
    m = max(A)
    exp = 1
    while (m / exp > 0):
        countingSort(A, exp)
        exp = exp * 10


# Main

# Take user input for the size of the array to be generated
n = int(input("Enter size of array:"))

# Generate an array of positive integers of size n;
# Each sorting algorithm has to sort the same generated array
A = generateArray(n)
B = A
C = A
D = A
E = A
F = A

# InsertionSort Runtime
start_timeA = time.time()
insertionSort(A, len(A))
print("Insertion Sort Time: ", (time.time() - start_timeA), " seconds")

# MergeSort Runtime
start_timeB = time.time()
mergeSort(B, 0, len(B) - 1)
print("Merge Sort Time: ", (time.time() - start_timeB), " seconds")

# HeapSort Runtime
start_timeC = time.time()
heapSort(C)
print("Heap Sort Time: ", (time.time() - start_timeC), " seconds")

# Quicksort Runtime
start_timeD = time.time()
quickSort(D, 0, len(D) - 1)
print("Quick Sort Time: ", (time.time() - start_timeD), " seconds")

# Randomized QuickSort Runtime
start_timeE = time.time()
quickSortR(E, 0, len(E) - 1)
print("Quick Sort (Random Pivot) Time: ", (time.time() - start_timeE), " seconds")

# RadixSortLSD Runtime
start_timeF = time.time()
radixSort(F)
print("Radix Sort Time: ", (time.time() - start_timeF), " seconds")