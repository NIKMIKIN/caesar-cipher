from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  #cycles through text shifting char if in alphabet
  for char in start_text:
    #if statement for whether or not message includes a non-letter
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")



#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
#printing logo imported from art
print(logo)
#prompting user
restart = True
#while loop to allow user to run program as many times as needed
while restart == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

#if user enters a shift > alphabet 
  if(shift >26):
    shift %= 26

  #calling caesar cipher function
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  decision = input("Type 'yes' if you want to go again. Otherwise type 'no'")
  if decision == 'yes':
    restart = True
  elif decision == 'no':
    restart = False