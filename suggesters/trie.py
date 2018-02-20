from typing import Generator, Sequence


class Node(object):
    """A Trie Node. Each node has a dictionary of children keyed on character"""

    def __init__(self):
        self.children = {}

    @property
    def is_leaf(self) -> bool:
        return len(self.children) < 1

    def insert(self, text: str) -> None:
        """Insert the given text into this Trie"""
        length = len(text)
        if (length < 1):
            return

        c = text[0]
        if c not in self.children:
            self.children[c] = Node()

        self.children[c].insert(text[1:])

    def find(self, path: str) -> 'Node':
        """Find a node that matches the given path string."""

        if len(path) < 1:
            return self
        else:
            c = path[0]
            if c in self.children:
                return self.children[c].find(path[1:])
            else:
                return None

    def leaves(self, path_from_root: str="") -> Generator[str, None, None]:
        """Produce a generator of the path strings for all the leaves reachable from this node.
        This does a depth-first traversal of the tree.

        Args:
            path_from_root (str): The path from the root to this node.
        """
        if self.is_leaf:
            yield path_from_root
        else:
            for c, node in self.children.items():
                path = path_from_root + c
                for leaf in node.leaves(path_from_root=path):
                    yield leaf


class TrieSuggester(object):
    """A suggester based on depth-first traversal of a Trie"""

    def __init__(self):
        self.root = Node()

    def index(self, suggestions: Sequence[str]) -> None:
        """Add the set of suggestions to the index."""

        for s in suggestions:
            self.root.insert(s)

    def search(self, prefix: str) -> Generator[str, None, None]:
        """Find suggestions that match the given prefix"""

        node = self.root.find(prefix)
        if not node:
            return None

        return node.leaves(path_from_root=prefix)
