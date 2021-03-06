from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.length = 0
        self.storage = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        current_node = self.storage.head
        if self.storage.length == 1:
            if key in current_node.value:
                return current_node.value[key]
        i = 1
        while (i<self.storage.length+1):
            if key in current_node.value:
                self.storage.move_to_front(current_node)
                return current_node.value[key] 
            current_node = current_node.next
            i += 1



    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if self.length < self.limit:
            self.length += 1
            self.storage.add_to_head({key:value})
        else:
            keyPresent = self.isKeyInStorage(key)
            print(keyPresent)
            if (keyPresent):
                self.storage.delete(keyPresent)
            else:
                self.storage.remove_from_tail()
            self.storage.add_to_head({key:value})
    
    def isKeyInStorage(self, key):
        i = 1
        current_node = self.storage.head
        print(self.storage.length)
        while (i<self.storage.length+1):
            print(current_node)
            if key in current_node.value:
                return current_node
            current_node = current_node.next
            i += 1
        return None

lru = LRUCache(3)
print('**********************************************************')
lru.set('item1','a')
print(lru.storage)
lru.set('item2','b')
print(lru.storage)
lru.set('item3','c')
print(lru.storage)
print(lru.get('item1'))
print(lru.storage)
lru.set('item4','d')
print(lru.storage)
print(lru.get('item1'))
print(lru.storage)
print(lru.get('item3'))
print(lru.storage)
print(lru.get('item4'))
print(lru.storage)
print(lru.get('item2'))
print(lru.storage)
print('**********************************************************')

