# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    word= sorted(word)
    anagram= sorted(anagram)
    sorted_word = "".join(word).lower()
    sorted_anagram = "".join(anagram).lower()

    if sorted_word == sorted_anagram:
        return True
    else:
        return False
print(find_anagram("Akolade Quam"," Akolade"))

