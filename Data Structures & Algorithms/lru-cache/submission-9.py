# custom class for doubly-linked list
class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # hash map that stores key -> node (key, value)
        self.start = Node(0, 0) # pointer that keeps track of left-most node (least recently used node)
        self.end = Node(0, 0) # pointer that keeps track of right-most node (most recently used node)

        # connect both start and end nodes bi-laterally
        self.start.next = self.end
        self.end.prev = self.start
        
    # helper function to remove node from linked list (and reorganize node pointers)
    def remove(self, node: Node) -> None:
        # first, get node reference on both sides
        prev = node.prev
        next = node.next

        # then, set pointers of those nodes to each other (main node is no longer connected to list)
        prev.next = next
        next.prev = prev

    # helper function to insert node at end linked list (and reorganizat node pointers)
    def insert(self, node: Node) -> None:
        # first, get node reference of current last node and our "end" (dummy) node
        prev = self.end.prev
        next = self.end

        # second, reorganize pointers so that last node <-> new node <-> end dummy node
        node.prev = prev
        node.next = next
        prev.next = node
        next.prev = node


    def get(self, key: int) -> int:
        # first check if key exists, then retrieve the value associated with key from hashmap
        # we also need to update that key and move to far right of our linked list as it was just used

        if key in self.cache:
            # TODO remove the node and re-add it to end of linked list
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # every operation will bump the key to the far right of our linked list as specified in description
        # we can just remove the key if exists, and re-add it
        
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # condition to check if capacity has been exceeded, if so, remove left-most node
        if len(self.cache) > self.capacity:
            oldest = self.start.next
            self.remove(oldest)
            del self.cache[oldest.key]

