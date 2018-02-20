from typing import Generator, Sequence, Dict, List


def ngrams(text: str, size: int, sentinel: str="_") -> Generator[str, None, None]:
    """Generate ngrams of the given size with sentinels padded at the begining, e.g.
    ngrams("foo", 2) -> ["_f", "fo", "oo"]

    Args:
        - text (str)
        - size (int)
        - sentinel (str): The sentinel to use for padding n-grams at the begining of the text.
    """
    padding = sentinel * (size - 1)
    text = padding + text
    length = len(text)
    end = length - size + 1
    for i in range(end):
        yield text[i:i + size]


class NGramSuggester(object):
    """A typo-tolerant suggester powered by an n-gram index."""

    def __init__(self, ngram_size: int=2) -> None:
        self.data: Dict[str, List[str]] = {}
        self.ngram_size = ngram_size

    def index(self, suggestions: Sequence[str]) -> None:
        """Add the set of suggestions to the index."""

        for s in suggestions:
            for ngram in ngrams(s, self.ngram_size):
                if ngram not in self.data:
                    self.data[ngram] = [s]
                else:
                    self.data[ngram].append(s)

    def search(self, prefix: str, match_percentage: float=0.9) -> Generator[str, None, None]:
        """Find suggestions that match the given prefix.

        Args:
            - prefix (str)
            - match_percentage (float): [0-1] the minimum percentage of n-grams that need to match for
              a suggestion to be returned. Lower values mean more fuzziness.
        """
        suggestions: dict = {}
        grams = list(ngrams(prefix, self.ngram_size))
        total_grams = len(grams)

        for ngram in grams:
            for s in self.data.get(ngram, []):
                if s in suggestions:
                    suggestions[s] += 1
                else:
                    suggestions[s] = 1

        for s, gram_count in suggestions.items():
            percentage = gram_count * 1.0 / total_grams
            if percentage > match_percentage:
                yield s
