def is_isogram(word):
    word = word.lower()  
    char_count = {}

    for char in word:
        if char.isalpha(): 
            if char in char_count:
                return False
            else:
                char_count[char] = 1

    return True

# Test the function
word = input("Enter a word: ")
if is_isogram(word):
    print(word, "is an isogram.")
else:
    print(word, "is not an isogram.")
