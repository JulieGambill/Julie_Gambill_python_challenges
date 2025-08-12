user_input = input("Please enter a phrase or word: ").lower()

def is_palindrome(text):
    # Remove spaces and check if the string is the same forwards and backwards
    cleaned = text.replace(" ", "")
    return cleaned == cleaned[::-1]

if is_palindrome(user_input):
    print("Yes, it's a palindrome!")
else:
    print("Not a palindrome.")
