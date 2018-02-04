import math

class MaxHeap:
    def __init__(self, list = None):
        self.list = [] if list is None else list

    def _index_of_parent(self, index_of_val):
        return int(math.floor(index_of_val / 2))

    def _index_of_left_child(self, index_of_val):
        return index_of_val * 2 + 1

    def _index_of_right_child(self, index_of_val):
        return index_of_val * 2 + 2

    def _index_out_of_bounds(self, index):
        return len(self.list) < index + 1

    def _swap_values(self, index1, index2):
        val = self.list[index1]
        self.list[index1] = self.list[index2]
        self.list[index2] = val

    def _index_of_bigger_child(self, index_of_val):
        left_index = self._index_of_left_child(index_of_val)
        if self._index_out_of_bounds(left_index):
            return None
        children = { left_index: self.list[left_index] }
        right_index = self._index_of_right_child(index_of_val)
        if self._index_out_of_bounds(right_index):
            children[right_index] = self.list[right_index]
        return max(children, key=children.get)

    def insert(self, val):
        index_of_val = len(self.list)
        self.list.append(val)

        def greater_than_parent(index_of_val):
            index_of_parent = self._index_of_parent(index_of_val)
            return self.list[index_of_val] > self.list[index_of_parent]

        while greater_than_parent(index_of_val):
            index_of_parent = self._index_of_parent(index_of_val)
            self._swap_values(index_of_val, index_of_parent)
            index_of_val = index_of_parent

        return self

    def extract(self):
        if len(self.list) is 0:
            return None

        top_val = self.list[0]
        self.list[0] = self.list.pop()

        index_of_val = 0
        while True:
            index_of_child = self._index_of_bigger_child(index_of_val)
            if index_of_child is None:
                break
            if self.list[index_of_child] > self.list[index_of_val]:
              self._swap_values(index_of_val, index_of_child)
              index_of_val = index_of_child
            else:
                break

        return top_val

    def sort(self):
        pass
