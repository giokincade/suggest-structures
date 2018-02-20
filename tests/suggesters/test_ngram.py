from unittest import TestCase
from suggesters.ngram import ngrams, NGramSuggester


class NGramSuggesterTest(TestCase):

    def test_ngrams(self):
        x = "f"
        self.assertEqual(list(ngrams(x, 2)), ["_f"])

        x = "fo"
        self.assertEqual(list(ngrams(x, 2)), ["_f", "fo"])

        x = "foo"
        self.assertEqual(list(ngrams(x, 2)), ["_f", "fo", "oo"])
        x = "food"
        self.assertEqual(list(ngrams(x, 2)), ["_f", "fo", "oo", "od"])

        x = "foo"
        self.assertEqual(list(ngrams(x, 3)), ["__f", "_fo", "foo"])
        x = "food"
        self.assertEqual(list(ngrams(x, 3)), ["__f", "_fo", "foo", "ood"])

    def test_fuzzy(self):
        suggester = NGramSuggester()
        data = ["foobar", "qux"]
        suggester.index(data)
        expected = ["foobar"]

        results = list(suggester.search("foba"))
        self.assertEqual(set(results), set(expected))

        results = list(suggester.search("fo"))
        self.assertEqual(set(results), set(expected))

        results = list(suggester.search("fob"))
        self.assertEqual(set(results), set(expected))

        results = list(suggester.search("f"))
        self.assertEqual(set(results), set(expected))
