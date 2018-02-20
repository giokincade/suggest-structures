from typing import Generator, Sequence
from bisect import bisect_left


class BinarySearchSuggester(object):
    """A simple suggester that keeps a sorted index and uses binary search to find suggestions."""

    def __init__(self):
        self.data = []

    def index(self, suggestions: Sequence[str]) -> None:
        """Add the set of suggestions to the index."""
        for s in suggestions:
            self.data.append(s)

        self.data.sort()

    def search(self, prefix: str) -> Generator[str, None, None]:
        """Find suggestions that match the given prefix"""

        # Perform a binary search to find where in the sorted list the prefix belongs.
        # Everything to the right will be lexicographically GTE than the prefix.
        start_position = bisect_left(self.data, prefix)

        for suggestion in self.data[start_position:]:
            if suggestion.startswith(prefix):
                yield suggestion
            else:
                break
