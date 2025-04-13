def first_substr(word, char):
    """Returns the first 3-character substring starting with the given character.
    If no such substring exists, returns None.
    """
    if not isinstance(word, str) or not isinstance(char, str) or len(char) != 1:
        return None

    for i in range(len(word)):
        if word[i] == char:
            # Check if there are at least 2 more characters after current position
            if i + 2 < len(word):
                return word[i:i + 3]
            break  # No need to check further if we found the first occurrence
    return None
