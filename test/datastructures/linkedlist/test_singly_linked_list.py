import unittest
from src.datastructures.linkedlist.singly_linked_list import SinglyLinkedList


class MyTestCase(unittest.TestCase):
    def test_empty_list(self):
        sll = SinglyLinkedList()
        self.assertEqual(sll.get(1), None)

    def test_addAtHead(self):
        sll = SinglyLinkedList()
        sll.addAtHead(10)
        self.assertEqual([node.value for node in sll], [10])

    def test_addAtTail(self):
        sll = SinglyLinkedList()
        sll.addAtTail(10)
        self.assertEqual([node.value for node in sll], [10])

    def test_addAtIndex(self):
        sll = SinglyLinkedList()
        sll.addAtIndex(0, 10)
        sll.addAtIndex(1, 20)
        sll.addAtIndex(2, 30)
        self.assertEqual([node.value for node in sll], [10, 20, 30])

    def test_get(self):
        sll = SinglyLinkedList()
        sll.addAtIndex(0, 10)
        sll.addAtIndex(1, 20)
        sll.addAtIndex(2, 30)
        self.assertEqual(sll.get(0), 10)
        self.assertEqual(sll.get(1), 20)
        self.assertEqual(sll.get(2), 30)

    def test_deleteAtIndex(self):
        sll = SinglyLinkedList()
        sll.addAtIndex(0, 10)
        sll.addAtIndex(1, 20)
        sll.addAtIndex(2, 30)
        sll.deleteAtIndex(0)
        self.assertEqual([node.value for node in sll], [20, 30])
        sll.deleteAtIndex(1)
        self.assertEqual([node.value for node in sll], [20])
        sll.deleteAtIndex(0)
        self.assertEqual([node.value for node in sll], [])

        # Below code tests deletion from an empty list
        sll.deleteAtIndex(0)
        self.assertEqual([node.value for node in sll], [])


if __name__ == '__main__':
    unittest.main()
