from logging import StreamHandler
from python.queue import Queue
from unittest.mock import patch
import unittest
import sys, io
sys.path.append("../")

from python import Stack, Queue

class DataStructureTests(unittest.TestCase):
    
    shared_instance = None
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.shared_instance = Stack("Kevin's Stack")
        cls.shared_queue = Queue("Kevin's Queue")
    
    def test_add_item_to_stack(self):
        self.shared_instance.push([1,2,3,4])
        self.shared_instance.push("1234")
        self.assertEqual(self.shared_instance.size(), 2)
    
    def test_remove_item_from_stack(self):
        
        self.shared_instance.pop()
        self.assertEqual(self.shared_instance.size(), 1)
    
    def test_add_item_to_queue(self):
        self.shared_queue.enqueue([1,2,3,4])
        self.shared_queue.enqueue("1234")
        self.assertEqual(self.shared_queue.size(), 2)
    
    def test_remove_item_from_queue(self):
        
        my_val = self.shared_queue.de`queue()
        self.assertEqual(my_val[1], 2)
        
#     def test_get_list_of_students_returns_list(self):
#         self.assertIsInstance((self.shared_instance.get_lists_of_students()),   list)
        
#     @patch('sys.stdout', new_callable=io.StringIO)
#     def test_list_students_output(self, mock_stdout):
#         self.shared_instance.list_students()
#         self.assertEqual(mock_stdout.getvalue().split('\n')[0], '1. Jessie 12335')
        
unittest.main()