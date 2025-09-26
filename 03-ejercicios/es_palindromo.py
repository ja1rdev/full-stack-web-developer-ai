import re

def es_palindromo(text):
    # Normalize text
    text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    
    # Check if it is a palindrome
    return text == text[::-1]

print(es_palindromo('Anita lava la tina'))