class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.data = [Node(0) for i in range(10000)]

    def add(self, key: int) -> None:
        index = key % len(self.data)
        node = self.data[index]

        while node.next:
            if node.next.val == key:
                return
            node = node.next
        node.next = Node(key)

    def remove(self, key: int) -> None:
        index = key % len(self.data)
        node = self.data[index]

        while node.next:
            if node.next.val == key:
                node.next = node.next.next
                return
            node = node.next
        

    def contains(self, key: int) -> bool:
        index = key % len(self.data)
        node = self.data[index]

        while node.next:
            if node.next.val == key:
                return True
            node = node.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)