from stegano import lsb

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                shifted = ((ord(char) - ord('a') + shift) % 26) + ord('a')
            elif char.isupper():
                shifted = ((ord(char) - ord('A') + shift) % 26) + ord('A')
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, 26 - shift)

extracted_message = lsb.reveal("secret_image.png")
print(extracted_message)

original_message = caesar_decrypt(extracted_message, 3)
print(original_message)