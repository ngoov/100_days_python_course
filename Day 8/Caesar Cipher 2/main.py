alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
def decrypt(cipher_text, shift_amount):
    original_text = ""
    for letter in cipher_text:
        original_position = alphabet.index(letter) - shift_amount
        original_position %= len(alphabet)
        original_text += alphabet[original_position]
    print(f"Here is the decoded result: {original_text}")

# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
def ceasar(text, shift_amount, direction):
    if direction == 'encode':
        encrypt(text, shift_amount)
    elif direction == 'decode':
        decrypt(text, shift_amount)
    else:
        print('Invalid action')

ceasar(text=text, shift_amount=shift, direction=direction)



