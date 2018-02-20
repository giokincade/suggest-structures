from unittest import TestCase
from suggesters import BruteForceSuggester, BinarySearchSuggester, EdgeNGramSuggester, NGramSuggester, TrieSuggester


class SuggesterTest(TestCase):

    def check_suggester(self, suggester):
        data = ["two", "one", "three", "foo", "bar"]
        suggester.index(data)
        results = list(suggester.search("t"))
        expected = ["two", "three"]
        self.assertEqual(set(results), set(expected))

    def test_brute(self):
        self.check_suggester(BruteForceSuggester())

    def test_binary_search(self):
        self.check_suggester(BinarySearchSuggester())

    def test_edge(self):
        self.check_suggester(EdgeNGramSuggester())

    def test_ngram(self):
        self.check_suggester(NGramSuggester())

    def test_trie(self):
        self.check_suggester(TrieSuggester())
