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
        self.assertEqual(b.insert(18).list, [18,2,10])
        self.assertEqual(b.insert(1).list, [18,2,10,1])
        self.assertEqual(b.insert(9).list, [18,9,10,1,2])
        self.assertEqual(b.insert(7).list, [18,9,10,1,2,7])
        self.assertEqual(b.insert(19).list, [19,9,18,1,2,7,10])

    def test_extract(self):
        b = MaxHeap([30, 25, 6, 23, 3, 5, 4, 7])
        self.assertEqual(b.extract(), 30)
        self.assertEqual(b.list, [25, 23, 6, 7, 3, 5, 4])
        self.assertEqual(MaxHeap().extract(), None)
        self.assertEqual(MaxHeap([233]).extract(), 233)

    def test__index_of_parent(self):
        b = MaxHeap([1,2,3,4,5,6])
        self.assertEqual(b._index_of_parent(6), 2)
        self.assertEqual(b._index_of_parent(5), 2)
        self.assertEqual(b._index_of_parent(4), 1)
        self.assertEqual(b._index_of_parent(3), 1)
        self.assertEqual(b._index_of_parent(2), 0)
        self.assertEqual(b._index_of_parent(1), 0)

    def test_build_heap(self):
        arr = [47, 92, 76, 83, 39, 70, 22, 2, 42, 54, 84, 26, 87, 77, 49]
        heap = [92, 84, 87, 83, 54, 76, 77, 2, 42, 47, 39, 26, 70, 22, 49]
        b = MaxHeap(arr).build_heap()
        self.assertEqual(b.list, heap)

if __name__ == "__main__":
    unittest.main()
