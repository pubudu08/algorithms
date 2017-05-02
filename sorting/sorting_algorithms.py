import math


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


def merge_sort(aList):
    """
    #  Statement:
    #  Given a disordered list of integers (or any other items),
    #  rearrange the integers in natural order.
    #
    #  Sample Input: [8,5,3,1,9,6,0,7,4,2,5]
    #
    #  Sample Output: [0,1,2,3,4,5,5,6,7,8,9]
    #
    #  Time Complexity of Solution:
    #  Best = Average = Worst = O(nlog(n)).
    #
    #  Approach:
    #   Merge sort is a divide and conquer algorithm. In the divide and
    #   conquer paradigm, a problem is broken into pieces where each piece
    #   still retains all the properties of the larger problem -- except
    #   its size. To solve the original problem, each piece is solved
    #   individually; then the pieces are merged back together.
    #
    #   For illustration, imagine needing to sort an array of 200 elements
    #   using selection sort. Since selection sort takes O(n^2), it would
    #   take about 40,000 time units to sort the array. Now imagine
    #   splitting the array into ten equal pieces and sorting each piece
    #   individually still using selection sort. Now it would take 400
    #   time units to sort each piece; for a grand total of 10400 = 4000.
    #   Once each piece is sorted, merging them back together would take
    #   about 200 time units; for a grand total of 200+4000 = 4,200.
    #   Clearly 4,200 is an impressive improvement over 40,000. Now
    #   imagine greater. Imagine splitting the original array into
    #   groups of two and then sorting them. In the end, it would take about
    #   1,000 time units to sort the array. That's how merge sort works.
    #
    #  NOTE to the Python experts:
    #     While it might seem more "Pythonic" to take such approach as
    #
    #         mid = len(aList) / 2
    #         left = mergesort(aList[:mid])
    #         right = mergesort(aList[mid:])
    #
    #     That approach take too much memory for creating sublists.
    """
    return splitter(aList, 0, len(aList) - 1)


def splitter(aList, first, last):
    # break problem into smaller structurally identical pieces
    mid = (first + last) // 2
    if first < last:
        splitter(aList, first, mid)
        splitter(aList, mid + 1, last)
    # merge solved pieces to get solution to original problem
    a, f, l = 0, first, mid + 1
    temp = [None] * (last - first + 1)

    while f <= mid and l <= last:
        if aList[f] < aList[l]:
            temp[a] = aList[f]
            f += 1
        else:
            temp[a] = aList[l]
            l += 1
        a += 1

    if f <= mid:
        temp[a:] = aList[f:mid + 1]

    if l <= last:
        temp[a:] = aList[l:last + 1]

    a = 0
    while first <= last:
        aList[first] = temp[a]
        first += 1
        a += 1
    return aList


# aList = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
# print(merge_sort(aList))


# Approach two
def merge_sort_approach_two(alist):
    # print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j += 1
            k += 1
    # print("Merging ", alist)
    return alist


# aList = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
# print(merge_sort_approach_two(aList))

def bucket_sort(A):
    """
    #  Statement:
    #  Given a disordered list of integers, rearrange them in natural
    #     order.
    #
    #  Sample Input: [8,5,3,1,9,6,0,7,4,2,5]
    #  Sample Output: [0,1,2,3,4,5,6,7,8,9,5]
    #
    #  Time Complexity of Solution:
    #  Best Case O(n); Average Case O(n); Worst Case O(n).
    #
    # Approach:
    # If it sounds too good to be true, then most likely it's not true.
    # Bucketsort is not an exception to this adage. For bucketsort to
    #   work at its blazing efficiency, there are multiple prerequisites.
    #   First the hash function that is used to partition the elements need
    #   to be very good and must produce ordered hash: if i < k then
    #   hash(i) < hash(k). Second, the elements to be sorted must be
    #   uniformly distributed.
    #
    # The aforementioned aside, bucket sort is actually very good
    #   considering that counting sort is reasonably speaking its upper
    #   bound. And counting sort is very fast. The particular distinction
    #   for bucket sort is that it uses a hash function to partition the
    #   keys of the input array, so that multiple keys may hash to the same
    #   bucket. Hence each bucket must effectively be a growable list;
    #   similar to radix sort.
    #
    # Numerous Internet sites, including university pages, have
    #   erroneously written counting sort code and call them bucket sort.
    #   Bucket sort uses a hash function to distribute keys; counting sort
    #   creates a bucket for each key. Indeed there are perhaps greater
    #   similarities between radix sort and bucket sort, than there are
    #   between counting sort and bucket sort.
    #
    # In the presented program insertionsort is used to sort
    #   each bucket. This is to inculcate that the bucket sort algorithm
    #   does not specify which sorting technique to use on the buckets.
    #   A programmer may choose to continuously use bucket sort on each
    #   bucket until the collection is sorted (in the manner of the radix
    #   sort program below). Whichever sorting method is used on the
    #   buckets, bucket sort still tends toward O(n).
    :return:
    """
    # get hash codes
    code = hashing(A)
    buckets = [list() for _ in range(code[1])]
    # distribute data into buckets: O(n)
    for i in A:
        x = re_hashing(i, code)
        buck = buckets[x]
        buck.append(i)

    # Sort each bucket: O(n).
    # I mentioned above that the worst case for bucket sort is counting
    # sort. That's because in the worst case, bucket sort may end up
    # with one bucket per key. In such case, sorting each bucket would
    # take 1^2 = O(1). Even after allowing for some probabilistic
    # variance, to sort each bucket would still take 2-1/n, which is
    # still a constant. Hence, sorting all the buckets takes O(n).

    for bucket in buckets:
        insertion_sort(bucket)
    ndx = 0
    # merge the buckets: O(n)
    for b in range(len(buckets)):
        for v in buckets[b]:
            A[ndx] = v
            ndx += 1


def hashing(A):
    m = A[0]
    for i in range(1, len(A)):
        if (m < A[i]):
            m = A[i]
    result = [m, int(math.sqrt(len(A)))]
    return result


def re_hashing(i, code):
    return int(i / code[0] * (code[1] - 1))


def selection_sort(aList):
    """
    Statement:
    #  Given a disordered list of integers (or any other items),
    #  rearrange the integers in natural order.
    #
    #  Sample Input: [18,5,3,1,19,6,0,7,4,2,5]
    #  Sample Output: [0,1,2,3,4,5,5,6,7,18,19]
    #
    #  Time Complexity of Solution:
    #  Best O(n^2); Average O(n^2); Worst O(n^2).
    #
    #  Approach:
    #  Selection sort is a step up from insertion sort from a memory
    #  viewpoint. It only swaps elements that need to be swapped. In terms
    #  of time complexity, however, insertion sort is better.
    """
    for i in range(len(aList)):
        least = i
        for k in range(i + 1, len(aList)):
            if aList[k] < aList[least]:
                least = k

        swap(aList, least, i)
