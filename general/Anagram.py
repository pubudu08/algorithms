from itertools import permutations


def anagrams(text):
    """Inits SampleClass with blah."""
    all_anagrams_parts = permutations(text)
    for anagram_parts in all_anagrams_parts:
        yield ''.join(anagram_parts)

        # for i in anagrams(text):
        #     print(i)

    # In [6]: for i in anagrams('abc'): print(i)
    # abc
    # acb
    # bac
    # bca
    # cab
    # cba


def is_anagram(text, original):
    return bool(text in frozenset(anagrams(original)))


    # In [8]: is_anagram('bacdc', 'dcbac')
    # Out[8]: True

    # In [9]: is_anagram('bacdc', 'dcbad')
    # Out[9]: False

    # (cinema,iceman), (host,shot) (aba,bab) (train,rain)


print(is_anagram("iceman", "cinema"))
print(is_anagram("shot", "host"))
print(is_anagram("bab", "aba"))
print(is_anagram("rain", "train"))
