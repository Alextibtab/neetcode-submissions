from typing import List

def contains_duplicate(words: List[str]) -> bool:
    for word in set(words):
        words.remove(word)
    if len(words) > 0:
        return True
    return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
