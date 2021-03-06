import unittest

from sorting.sorting_algorithms import counting_sort, bubble_sort, radix_sort, insertion_sort, merge_sort,\
    merge_sort_approach_two, bucket_sort, selection_sort, quick_sort, heap_sort, cycle_sort


class Test(unittest.TestCase):
    def test_counting_sort(self):
        counting_sort_list = [6, 4, 3, 2, 1, 4, 3, 6, 6, 2, 4, 3, 4]
        k = 6
        counting_sort(counting_sort_list, k)
        for i in range(1, len(counting_sort_list)):
            if counting_sort_list[i - 1] > counting_sort_list[i]:
                self.fail("counting sort method fails.")

    def test_bubble_sort(self):
        bubble_sort_list = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
        bubble_sort(bubble_sort_list)
        for i in range(1, len(bubble_sort_list)):
            if bubble_sort_list[i - 1] > bubble_sort_list[i]:
                self.fail("bubble_sort method fails.")

    def test_radix_sort(self):
        radix_sort_list = [18, 5, 100, 3, 1, 19, 6, 0, 7, 4, 2]
        radix_sort(radix_sort_list)
        for i in range(1, len(radix_sort_list)):
            if radix_sort_list[i - 1] > radix_sort_list[i]:
                self.fail("radix_sort method fails.")

    def test_insertion_sort(self):
        insertion_sort_list = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
        insertion_sort(insertion_sort_list)
        for i in range(1, len(insertion_sort_list)):
            if insertion_sort_list[i - 1] > insertion_sort_list[i]:
                self.fail("insertion_sort method fails.")

    def test_merge_sort(self):
        merge_sort_list = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
        merge_sort(merge_sort_list)
        for i in range(1, len(merge_sort_list)):
            if merge_sort_list[i - 1] > merge_sort_list[i]:
                self.fail("merge_sort method fails.")

    def test_merge_sort_approach_two(self):
        merge_sort_list = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
        merge_sort_approach_two(merge_sort_list)
        for i in range(1, len(merge_sort_list)):
            if merge_sort_list[i - 1] > merge_sort_list[i]:
                self.fail("merge_sort_approach_two method fails.")

    def test_bucket_sort(self):
        bucket_sort_list = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
        bucket_sort(bucket_sort_list)
        for i in range(1, len(bucket_sort_list)):
            if bucket_sort_list[i - 1] > bucket_sort_list[i]:
                self.fail("bucket_sort method fails.")

    def test_selection_sort(self):
        selection_sort_list = [18, 5, 3, 1, 19, 6, 0, 7, 4, 2, 5]
        selection_sort(selection_sort_list)
        for i in range(1, len(selection_sort_list)):
            if selection_sort_list[i - 1] > selection_sort_list[i]:
                self.fail("selection_sort method fails.")

    def test_quick_sort(self):
        quick_sort_list = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2]
        quick_sort(quick_sort_list)
        for i in range(1, len(quick_sort_list)):
            if quick_sort_list[i - 1] > quick_sort_list[i]:
                self.fail("quick_sort method fails.")

    def test_heap_sort(self):
        heap_sort_list = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2]
        heap_sort(heap_sort_list)
        for i in range(1, len(heap_sort_list)):
            if heap_sort_list[i - 1] > heap_sort_list[i]:
                self.fail("quick_sort method fails.")

    def test_cycle_sort(self):
        cycle_sort_list = [0, 1, 2, 2, 2, 2, 1, 9, 3.5, 5, 8, 4, 7, 0, 6]
        cycle_sort(cycle_sort_list)
        for i in range(1, len(cycle_sort_list)):
            if cycle_sort_list[i - 1] > cycle_sort_list[i]:
                self.fail("quick_sort method fails.")