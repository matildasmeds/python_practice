import math

class MaxHeap:
    def __init__(self, list = None):
        self.list = [] if list is None else list

    def _index_of_parent(self, index_of_val):
        val = int(math.floor((index_of_val - 1) / 2))
        if val < 0: return None
        return val

    def _index_of_left_child(self, index_of_val):
        return index_of_val * 2 + 1

    def _index_of_right_child(self, index_of_val):
        return index_of_val * 2 + 2

    def _index_out_of_bounds(self, index):
        return len(self.list) < index + 1

    def _swap(self, index1, index2):
        val = self.list[index1]
        self.list[index1] = self.list[index2]
        self.list[index2] = val

    def _index_of_bigger_child(self, index_of_val):
        left = self._index_of_left_child(index_of_val)
        if self._index_out_of_bounds(left): return None

        right = self._index_of_right_child(index_of_val)
        if self._index_out_of_bounds(right): return left
        if self.list[left] > self.list[right]: return left
        return right

    def insert(self, val):
        index_of_val = len(self.list)
        self.list.append(val)

        def greater_than_parent(index_of_val):
            if index_of_val is 0: return False # no parent
            parent = self._index_of_parent(index_of_val)
            return self.list[index_of_val] > self.list[parent]

        while greater_than_parent(index_of_val):
            parent = self._index_of_parent(index_of_val)
            self._swap(index_of_val, parent)
            index_of_val = parent

        return self

    def extract(self):
        if len(self.list) is 0: return None
        if len(self.list) is 1: return self.list.pop()

        top_val = self.list[0]
        self.list[0] = self.list.pop()
        index_of_val = 0
        while True:
            child = self._index_of_bigger_child(index_of_val)
            if child is None: break
            # works assuming the heap already had heap property
            if self.list[child] > self.list[index_of_val]:
                self._swap(index_of_val, child)
                index_of_val = child
            else: break

        return top_val

    def _heapify_subtree(self, root):
        child = self._index_of_bigger_child(root)
        if child is None: return
        # Swap root with bigger child
        if self.list[child] > self.list[root]:
            self._swap(root, child)
        # Recursive calls for each children
        left = self._index_of_left_child(root)
        if left is None: return
        self._heapify_subtree(left)
        right = self._index_of_right_child(root)
        if right is None: return
        self._heapify_subtree(right)

    # Applying Floyd method for restoring heap property for
    # a random list
    def build_heap(self):
        if len(self.list) < 2: return self # can't be sorted
        last = len(self.list) - 1
        while True:
            parent = self._index_of_parent(last)
            self._heapify_subtree(parent)
            last -= 1
            if last is 0: break
        return self
