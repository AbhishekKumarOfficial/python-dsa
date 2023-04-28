import unittest
from src.datastructures.tree.trie import Trie


class TestTrie(unittest.TestCase):
    def test_all(self):
        trie = Trie()
        trie.insert("apple")
        self.assertEqual(trie.search("apple"), True)
        self.assertEqual(trie.search("app"), False)
        self.assertEqual(trie.startsWith("app"), True)
        trie.insert("app")
        self.assertEqual(trie.search("app"), True)


if __name__ == '__main__':
    unittest.main()
