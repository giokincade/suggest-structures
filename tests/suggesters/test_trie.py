from unittest import TestCase
from suggesters.trie import Node


class TrieSuggesterTest(TestCase):

    def test_node(self):
        text = "food"
        root = Node()
        root.insert(text)

        node = root
        for c in text:
            assert(c in node.children)
            assert(not node.is_leaf)
            node = node.children[c]

        assert(node.is_leaf)

    def test_leaves(self):
        words = ["foo", "bar"]
        root = Node()
        for w in words:
            root.insert(w)

        self.assertEqual(words, list(root.leaves()))

    def test_find(self):
        words = ["foo", "bar"]
        root = Node()
        for w in words:
            root.insert(w)

        self.assertEqual(None, root.find("qux"))
        self.assertEqual(["foo"], list(root.find("f").leaves("f")))
        self.assertEqual(["foo"], list(root.find("fo").leaves("fo")))
        self.assertEqual(["foo"], list(root.find("foo").leaves("foo")))
