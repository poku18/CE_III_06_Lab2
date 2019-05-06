import unittest
from lab2 import insertionSort, mergeSort

class SearchTestCase(unittest.TestCase):
    # Tests for binary search
    def testinsertionSort(self):
            unsorted1= [5,3,1,2,4]
            unsorted2= [8, 9, 7, 5,3]
            
            values1 = [1, 2, 3 , 4, 5]
            values2 = [3,5,7,8,9]
            self.assertEqual(insertionSort(unsorted1),values1)
            self.assertEqual(insertionSort(unsorted2),values2)
            
            self.assertEqual(mergeSort(unsorted1),values1)
            self.assertEqual(mergeSort(unsorted2),values2)
        
if __name__ == '__main__':
    unittest.main()
