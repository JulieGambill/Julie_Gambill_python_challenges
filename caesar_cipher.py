def caesar_cipher(text, shift):
    result = ''
    shift %= 26
    for char in text:
        if char.isalpha():
            if char.isupper():
                start_ascii = ord('A')
                shifted_char_ascii = (ord(char) - start_ascii + shift) % 26 + start_ascii
                result += chr(shifted_char_ascii)
            else:
                start_ascii = ord('a')
                shifted_char_ascii = (ord(char) - start_ascii + shift) % 26 + start_ascii
                result += chr(shifted_char_ascii)
        else:
            result += char
    return result
user_input = input("Enter text: ")
shift_value = int(input("Enter shift value: "))
print(caesar_cipher(user_input, shift_value))