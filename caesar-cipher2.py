alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(plain_text, shift_amount):
  text = ""
  if direction == "encode":
    for letter in plain_text:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      text = text + alphabet[new_position]
    print(f"The encoded text is {text}")
  elif direction == "decode":
    for letter in plain_text:
      position = alphabet.index(letter)
      new_position = position - shift_amount
      text = text + alphabet[new_position]
    print(f"The decoded text is {text}") 
# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1
#   for letter in start_text:
#     position = alphabet.index(letter) 
#     new_position = position + shift_amount
#     end_text += alphabet[new_position]
#   print(f" Here's the {direction}d result {end_text}")



#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(plain_text = text, shift_amount=shift)
# caesar(start_text = text, shift_amount = shift, cipher_direction = direction)