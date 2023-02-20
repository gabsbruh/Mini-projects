alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text : str, shift : int, direction : str) -> str:
    """Function that encrypting or decrypting word/sentence in caesar cipher

    Args:
        text (str): word/sentence which you want to encrypt/decrypt
        shift (int): number of shifts in alphabet
        direction (str): 'encode' / 'decode' - describe what u want to do

    Returns:
        str: encrypted / decrypted string
    """
    crypted_text = ""
    for letter in text:
        try:
            if direction == "encode":
                shifted_index = alphabet.index(letter) + shift
            elif direction == "decode":
                shifted_index = alphabet.index(letter) - shift
            crypted_text += alphabet[shifted_index % len(alphabet)] # % len alphabet used to loop the alphabet (without this encrypting ast letter of the alphabet can be a problem)
        except:
            crypted_text += letter
    return print(crypted_text)
            
# run 
again = True
while again == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))        
    print(caesar(text, shift, direction))
    again_input = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")  
    if again_input == 'no':
        again = False
        print('\nGoodbye!')
    elif again_input == 'yes':
        again == True
    else:
        print("You typed wrong answer!")
        
    
        
    

