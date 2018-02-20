from typing import Generator, Sequence


class BruteForceSuggester(object):
    """A simple suggester that scans through the entire suggestion corpus."""

    def __init__(self):
        self.data = []

    def index(self, suggestions: Sequence[str]) -> None:
        """Add the set of suggestions to the index."""
        for s in suggestions:
            self.data.append(s)

    def search(self, prefix: str) -> Generator[str, None, None]:
        """Find suggestions that match the given prefix"""
        for s in self.data:
            if s.startswith(prefix):
                yield s
