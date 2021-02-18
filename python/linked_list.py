class LinkList:
  # write your __init__ method here that should store a 'head' value which is the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  
  def __init__(self,data) -> None:
      self.head =None    
      self.length = 0  
  def add(self, data):
    # write your code to ADD an element to the Linked List
      new_node = Node(data)
      old_node = self.head
      self.head = new_node
      self.head.next = old_node
      self.length +=1
      pass
  def remove(self,target):
      current = self.head
      prev = None
      while current:
          if current.data == target:
              if prev:
                  prev.ext = current.next
              else:
                  self.head = current.next
              return True 
      prev = current
      current = current.next
      return False

  def get(self, element_to_get):
    # write you code to GET and return an element from the Linked List
    pass

# ----- Node ------
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
  # store your DATA and NEXT values here
    pass

