def is_anagram(test, original):
    char_count = {}
    for test, original in zip(test, original):
        char_count[test] = char_count.get(test, 0) + 1
        char_count[original] = char_count.get(original, 0) - 1
    
    return all(value == 0 for value in char_count.values())