# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

def autocomplete(words: list, substr: str):
    response = []
    substr_lenght = len(substr)
    for word in words:
        word_length = len(word)
        if word_length < substr_lenght:
            continue

        if word[0:substr_lenght] == substr:
            response.append(word)

    return response


print(autocomplete(["deer", "dead", "dog", "diog", "d"], "de"))
