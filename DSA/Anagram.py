from collections import Counter
def anagram(first,second):
    if Counter(first)==Counter(second):
        return "Anagram"
    return "Not Anagram"

print(anagram("rat","tar"))