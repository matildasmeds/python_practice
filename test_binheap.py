from binheap import MaxHeap
import unittest

class TestMaxHeap(unittest.TestCase):
    def test_init(self):
        self.assertEqual(MaxHeap().list, [])
        self.assertEqual(MaxHeap([]).list, [])
        self.assertEqual(MaxHeap(None).list, [])
        self.assertEqual(MaxHeap([1,2,3,4,5,6]).list, [1,2,3,4,5,6])

    def test_insert(self):
        b = MaxHeap()
        self.assertEqual(b.insert(2).list, [2])
        self.assertEqual(b.insert(10).list, [10,2])
        self.assertEqual(b.insert(18).list, [18,10,2])
        self.assertEqual(b.insert(1).list, [18,10,2,1])

    def test_extract(self):
        b = MaxHeap([30, 25, 6, 23, 3, 5, 4, 7])
        self.assertEqual(b.extract(), 30)
        self.assertEqual(b.list, [25, 23, 6, 7, 3, 5, 4])
        self.assertEqual(MaxHeap().extract(), None)

    @unittest.skip("not implemented yet")
    def sort():
        b = MaxHeap([[3, 7, 6, 25, 5, 23, 4]])
        self.assertEqual(b.sort().list, [25, 7, 23, 3, 5, 6, 4])

if __name__ == "__main__":
    unittest.main()
