def counting_sort(aList, k):
    """
     counting sort is an algorithm for sorting a collection of objects according to keys that are small integers;
     that is, it is an integer sorting algorithm.
     It operates by counting the number of objects that have each distinct key value,
     and using arithmetic on those counts to determine the positions of each key value in the output sequence.
     Its running time is linear in the number of items and the difference between the maximum and minimum key values,
     so it is only suitable for direct use in situations
     where the variation in keys is not significantly greater than the number of items.

    Given a disordered list of repeated integers, rearrange the integers in natural order.
     Sample Input: [4,3,2,1,4,3,2,4,3,4]
     Sample Output: [1,2,2,3,3,3,4,4,4,4]

     Time Complexity of Solution:
     Best Case O(n+k); Average Case O(n+k); Worst Case O(n+k),
     where n is the size of the input array and k means the values range from 0 to k

    #  Approach:
    #  Counting sort, like radix sort and bucket sort,
    #  is an integer based algorithm (i.e. the values of the input
    #  array are assumed to be integers). Hence counting sort is
    #  among the fastest sorting algorithms around, in theory. The
    #  particular distinction for counting sort is that it creates
    #  a bucket for each value and keep a counter in each bucket.
    #  Then each time a value is encountered in the input collection,
    #  the appropriate counter is incremented. Because counting sort
    #  creates a bucket for each value, an imposing restriction is
    #  that the maximum value in the input array be known beforehand.
    #
    #  There is a great number of counting sort code on the Internet,
    #  including on university websites, that erroneously claim to be
    #  bucket sort. Bucket sort uses a hash function to distribute
    #  values; counting sort, on the other hand, creates a counter for
    #  each value -- hence the name.
    #
    #  Implementation notes:
    #
    #  1] Since the values range from 0 to k, create k+1 buckets.
    #  2] To fill the buckets, iterate through the input list and
    #  each time a value appears, increment the counter in its
    #  bucket.
    #  3] Now fill the input list with the compressed data in the
    #  buckets. Each bucket's key represents a value in the
    #  array. So for each bucket, from smallest key to largest,
    #  add the index of the bucket to the input array and
    #  decrease the counter in said bucket by one; until the
    #  counter is zero.
    #=======================================================================
    """
    counter = [0] * (k + 1)
    for i in aList:
        counter[i] += 1
    ndx = 0
    for i in range(len(counter)):
        while 0 < counter[i]:
            aList[ndx] = i
            ndx += 1
            counter[i] -= 1
    return aList


def bubble_sort(A):
    """
    #  Statement:
    #  Given a disordered list of integers (or any other items),
    #  rearrange the integers in natural order.
    #
    #  Sample Input: [8,5,3,1,9,6,0,7,4,2,5]
    #  Sample Output: [0,1,2,3,4,5,5,6,7,8,9]
    #
    # Time Complexity of Solution:
    #  Best O(n^2); Average O(n^2); Worst O(n^2).
    #
    #  Approach:
    #   Bubblesort is an elementary sorting algorithm. The idea is to
    #   imagine bubbling the smallest elements of a (vertical) array to the
    #   top; then bubble the next smallest; then so on until the entire
    #   array is sorted. Bubble sort is worse than both insertion sort and
    #   selection sort. It moves elements as many times as insertion sort
    #   (bad) and it takes as long as selection sort (bad). On the positive
    #   side, bubble sort is easy to understand. Also there are highly
    #   improved variants of bubble sort.
    #
    #  0] For each element at index i from 0 to n, loop:
    #  1] For each element at index k, from n to i exclusive, loop:
    #  2] If the element at k is less than that at k-1, swap them.
    """
    for i in range(len(A)):
        for k in range(len(A) - 1, i, -1):
            if (A[k] < A[k - 1]):
                swap(A, k, k - 1)
    return A


def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


def radix_sort(aList):
    """
    # aList = [4,3,2,1,4,3,2,4,3,4]
    # print(counting_sort(aList,6))
    # aList_bubble = [8,5,3,1,9,6,0,7,4,2,5]
    # print(bubble_sort(alist_bubble))

    #  Statement:
    #  Given a disordered list of integers, rearrange them in natural order.
    #
    #  Sample Input: [18,5,100,3,1,19,6,0,7,4,2]
    #
    #  Sample Output: [0,1,2,3,4,5,6,7,18,19,100]
    #
    #  Time Complexity of Solution:
    #  Best Case O(kn); Average Case O(kn); Worst Case O(kn),
    #  where k is the length of the longest number and n is the
    #  size of the input array.
    #
    #  Note: if k is greater than log(n) then an nlog(n) algorithm would
    #  be a better fit. In reality we can always change the radix
    #  to make k less than log(n).
    #
    #  Approach:
    #  radix sort, like counting sort and bucket sort, is an integer based
    #  algorithm (i.e. the values of the input array are assumed to be
    #  integers). Hence radix sort is among the fastest sorting algorithms
    #  around, in theory. The particular distinction for radix sort is
    #  that it creates a bucket for each cipher (i.e. digit); as such,
    #  similar to bucket sort, each bucket in radix sort must be a
    #  growable list that may admit different keys.
    #
    #  For decimal values, the number of buckets is 10, as the decimal
    #  system has 10 numerals/cyphers (i.e. 0,1,2,3,4,5,6,7,8,9). Then
    #  the keys are continuously sorted by significant digits.
    """
    r_a_d_i_x = 10
    max_length = False
    tmp, placement = -1, 1

    while not max_length:
        max_length = True
        # declare and initialize buckets
        buckets = [list() for _ in range(r_a_d_i_x)]
        # split aList between lists
        for i in aList:
            tmp = int(i / placement)
            buckets[tmp % r_a_d_i_x].append(i)
            if max_length and tmp > 0:
                max_length = False
        # empty lists into aList array
        a = 0
        for b in range(r_a_d_i_x):
            buck = buckets[b]
            for i in buck:
                aList[a] = i
                a += 1
        # move to next digit
        placement *= r_a_d_i_x
    return aList

    # alist_radix = [18,5,100,3,1,19,6,0,7,4,2];
    # print(radix_sort(alist_radix))


def insertion_sort(aList):
    """
    #  Statement:
    #  Given a disordered list of integers (or any other items),
    #  rearrange the integers in natural order.
    #
    #  Sample Input: [8,5,3,1,9,6,0,7,4,2,5]
    #  Sample Output: [0,1,2,3,4,5,5,6,7,8,9]
    #
    #  Time Complexity of Solution:
    #  Best O(n); Average O(n^2); Worst O(n^2).
    #
    #  Approach:
    #  Insertion sort is good for collections that are very small
    #  or nearly sorted. Otherwise it's not a good sorting algorithm:
    #  it moves data around too much. Each time an insertion is made,
    #  all elements in a greater position are shifted.
    :param aList: unsorted list
    :return: aList sorted list based on natural order
    """
    for i in range(1, len(aList)):
        tmp = aList[i]
        k = i
        while k > 0 and tmp < aList[k - 1]:
            aList[k] = aList[k - 1]
            k -= 1
        aList[k] = tmp

    return aList
