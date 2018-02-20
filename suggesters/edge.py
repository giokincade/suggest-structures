from typing import Generator, Sequence


class EdgeNGramSuggester(object):
    """A simple suggester that keeps a dictionary from prefixes to suggestions."""

    def __init__(self):
        self.data = {}

    def index(self, suggestions: Sequence[str]) -> None:
        """Add the set of suggestions to the index."""
        for s in suggestions:
            for i in range(len(s)):
                ngram = s[0:i + 1]
                if ngram not in self.data:
                    self.data[ngram] = [s]
                else:
                    self.data[ngram].append(s)

    def search(self, prefix: str) -> Generator[str, None, None]:
        """Find suggestions that match the given prefix"""

        if prefix in self.data:
            for s in self.data[prefix]:
                yield s
        else:
            return None
