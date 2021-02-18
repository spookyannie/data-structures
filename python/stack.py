class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
  def __init__(self, name) -> None:
      self.name = name
      self.my_stack = []
      self.total = len(self.my_stack)
      pass

  def push(self, item):
    # write your code to add data following LIFO and return the Stack
    self.my_stack.append(item)
    self.total = len(self.my_stack)
    
    pass

  def pop(self):
    # write your code to removes the data following LIFO and return the Stack
    return self.my_stack.pop()
    pass

  def size(self):
    # write your code that returns the size of the Stack
    self.total = len(self.my_stack)
    return len(self.my_stack)
    pass
