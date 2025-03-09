def groupAnagrams(strs):
    """
    this function groups anagrams together and retruns a list of list of anagrams

    anagrams are words that have the same letters but in different order

    args:
    strs: list of strings

    return: list of list of anagrams separated in groups

    Examples:
    >>> groupAnagrams([""]):
    [[""]]

    >>> groupAnagrams(["a"]):
    [["a"]]

    >>> groupAnagrams(["eat","tea","tan","ate","nat","bat"]):
    [['eat', 'tea', 'ate'], ['tan', 'nat'],['bat']]

    >>> groupAnagrams(["ate","nat","bat", "tab"]):
    [["bat", "tab"], ['nat'],["ate"]]
    """

    # create a dictionary to store the anagrams
    anagrams_dict = {}

    # iterate through each word in list and sort it
    for word in strs:
        sorted_word = "".join(sorted(word))
        # if the sorted word is already in the dictionary append the it to the list of anagrams of that sorted word as key
        if sorted_word in anagrams_dict.keys():
            anagrams_dict[sorted_word].append(word)

        # if the sorted word is not in the dictionary add it as key and the word as the first element of the list
        else:
            anagrams_dict[sorted_word] = [word]

    # create a list to store the groups of anagrams all in one list
    anagrams_list = []

    # iterate through the values of the anagrams_dict and append them to the list
    for anagrams in anagrams_dict.values():
        anagrams_list.append(anagrams)

    # return list of lists of anagrams
    return anagrams_list
