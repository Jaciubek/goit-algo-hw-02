from collections import deque

def is_palindrome(cleaned_string):
    # Remove spaces and convert to lower case this string
    cleaned_string = ''.join(char.lower() for char in cleaned_string if char.isalnum())
    
    # Create a deque (dubleside queue) and add all characters from the cleaned string
    char_deque = deque(cleaned_string)
    
    # Check if a string is a palindrome
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True

# Example usage:
sample_string_1 = "Madam, I’m Adam"
sample_string_2 = "Madam, I’m Ann"
print(f"'{sample_string_1}' jest palindromem? {is_palindrome(sample_string_1)}")
print(f"'{sample_string_2}' jest palindromem? {is_palindrome(sample_string_2)}")