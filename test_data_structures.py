from logging import StreamHandler
from python.queue import Queue
from unittest.mock import patch
import unittest
import sys, io
sys.path.append("../")

from python import Stack, Queue, LinkList

class DataStructureTests(unittest.TestCase):
    
    shared_instance = None
    
    @classmethod
    def setUpClass(cls) -> None:
        
        cls.shared_instance = Stack("Kevin's Stack")
        cls.shared_queue = Queue("Kevin's Queue")
        cls.shared_linklist = LinkList("Kevin's Linked List")
        
    def test_add_item_to_stack(self):
        """"This will test adding an item to the stack """
        
        self.shared_instance.push([1,2,3,4])
        self.shared_instance.push("1234")
        self.assertEqual(self.shared_instance.size(), 2)
    
    def test_remove_item_from_stack(self):
        """"This will test removing an item from the stack"""
        self.shared_instance.pop()
        self.assertEqual(self.shared_instance.size(), 1)
    
    def test_add_item_to_queue(self):
        """This will test adding an item to the queue"""
        self.shared_queue.enqueue([1,2,3,4])
        self.shared_queue.enqueue("1234")
        self.assertEqual(self.shared_queue.size(), 2)
    
    def test_remove_item_from_queue(self):
        """This will test removing an item from the queue"""
        my_val = self.shared_queue.dequeue()
        self.assertEqual(my_val[1], 2)
    
    def test_adding_linklist(self):
        """This will test adding stuff to a linked list"""
        self.shared_linklist.add("1")
        self.shared_linklist.add("2")
        self.shared_linklist.add("3")
        self.assertEqual(self.shared_linklist.head.data, '3')
    def test_length_linklist(self):
        """This will test to see how many items are in are linked list"""
        self.assertEqual(self.shared_linklist.length, 3)
    # def test_search_linklist(self):
    #     """This will test to see if our search function works: True"""
    #     self.assertEqual(self.shared_linklist.search('2'), True)
    # def test_search_linklist(self):
    #     """This will test to see if our search function works: False"""
    #     self.assertEqual(self.shared_linklist.search('31'), False)
    # def test_remove_item_linklist(self):
    #     """ this will test to remove an item in our linked list"""
    #     self.shared_linklist.remove('1')
    #     self.assertEqual(self.shared_linklist.head.data, '3')
    # def test_search_linklist(self):
    #     """This will test to see if our search function works after removing the number 1: False"""
    #     self.assertEqual(self.shared_linklist.remove('1'), False)
unittest.main()