
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(start_text, shift_amount):
  encrypted_text = ""
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      shifted_position = (position + shift_amount)
      if position + shift_amount > len(alphabet)-1:
         shifted_position = (position + shift_amount) - (len(alphabet))
      elif position + shift_amount <= len(alphabet)-1:
        shifted_position = (position + shift_amount)
      encrypted_text += alphabet[shifted_position]
    else:
        encrypted_text += char
  print(f"Here's your message: {encrypted_text}")

def decrypt(start_text, shift_amount):
  encrypt(start_text, -shift_amount)


def cipher (start_text, shift_amount, cipher_direction):
  if direction == "encode":
    encrypt(start_text, shift_amount)
  elif direction == "decode":
    decrypt(start_text, shift_amount)
  else:
    print("Wrong input")



# def encrypt(text, shift):
#   encrypted_text = ""
#   for char in text:
#       if char in alphabet:
#           position = alphabet.index(char)
#           shifted_position = (position + shift) % len(alphabet)
#           encrypted_text += alphabet[shifted_position]
#       else:
#           encrypted_text += char  # Keep non-alphabetic characters unchanged
#   return encrypted_text


counter = True
while counter:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift%26
  cipher(start_text=text, shift_amount=shift, cipher_direction=direction)
  ask_again = input ("Do you want to try again? (y/n)\n").lower()
  if ask_again == "n" or ask_again == "no":
    counter = False
    print("Bye")
  elif ask_again == "y" or ask_again == "yes":
    counter = True
  else:
    print("Wrong input")
    counter = False

