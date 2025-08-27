def count_vowels(word):
    vowels = ["a", "e", "i", "o","u"]
    count = 0
    word_lower = word.lower()
    for char in word_lower:
        if char in vowels:
            count += 1
    return count

word = input("Enter the text string: ")
print(f"The text string {word} has {count_vowels(word)} vowels")        