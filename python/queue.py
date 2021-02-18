class Queue:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue
  def __init__(self, name) -> None:
      self.name = name
      self.my_queue = []
      self.total = len(self.my_queue)
      pass
  
  def enqueue(self, item):
    # write your code to add data to the Queue following FIFO and return the Queue
    self.my_queue.append(item)
    pass

  def dequeue(self):
    # write your code to removes the data to the Queue following FIFO and return the Queue
    return self.my_queue.pop(0)
    
  def size(self):
    # write your code that returns the size of the Queue
    self.total = len(self.my_queue)
    return len(self.my_queue)
    pass
