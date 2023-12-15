from typing import Callable
import unittest

import sorts
from data import create_random_array


class SortTestCase(unittest.TestCase):

    arrays = [
        [2187, 9039, 1853, -9087, -1305, 1992, -6454, -9956, 8300, 8392],
        [-3611, 243, 1826, 5499, 4014, -6939, -8021, -1050, 9047, -3233],
        [6797, 2441, -4376, 6791, 9953, 6304, -4996, 5314, -9848, -6863],
        [-5321, 713, -6225, -2583, -2190, 1701, -2491, -2108, -9995, -8457],
        [9235, 7216, -6261, -1468, 1080, -5712, 7466, -1343, 7828, 3232],
    ]

    def fuzzy_test(self, algorithm: Callable[[list[int]], None]):

        for _ in range(100):
            array = create_random_array(10)
            a_1, a_2 = array.copy(), array.copy()
            algorithm(a_1)
            a_2.sort()
            self.assertEqual(a_1, a_2)

    def __test_algorithm(self, algorithm: Callable[[list[int]], None]):

        for a in self.arrays:
            a_1, a_2 = a.copy(), a.copy()
            algorithm(a_1)
            a_2.sort()
            self.assertEqual(a_1, a_2)

        self.fuzzy_test(sorts.bubble_sort)

    def test_algorithms(self):
        algorithms = [
            sorts.bubble_sort,
            sorts.insertion_sort,
            sorts.selection_sort,
            sorts.shell_sort,
            # fast algorithms
            sorts.quick_sort,
            sorts.heap_sort,
            sorts.merge_sort,
        ]

        for algorithm in algorithms:
            self.__test_algorithm(algorithm)
            self.fuzzy_test(algorithm)
