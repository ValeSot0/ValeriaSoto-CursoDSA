from Node import Node
class Stack:
    def __init__(self, top_item = None):
        self.top_item = top_item

    def push(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.top_item)
        self.top_item = new_node

    def pop(self):
        if self.top_item is None:
            return None
        item_to_remove = self.top_item
        self.top_item = self.top_item.get_next_node()
        return item_to_remove.get_value()
    
    def peek(self):
        return self.top_item.get_value()