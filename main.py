# Morse Code Dictionary
code = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 
    'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', 
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

# Reverse morse code dictionary for Decoding
reverse_code = {values : key for key, values in code.items()}

def translate_to_morse(text):
    """
    Translate a given text into morse code
    
    Args:
    text (str): The inp[ut text to be translated.
    
    Returns:
    str: The translated morse code.
    """
    morse = ""
    for char in text:
        if char.lower() in code:
            morse += code[char.lower()] + " " # Add morse code for each character followed by space
        elif char == " ":
            morse += "/ "    # Use "/" to represent space between words
    return morse.strip()     # Remove trailing space

def translate_to_text(morse):
    """
    Translate morse code back into plain text
    
    Args:
    morse (str): The input morse code to be translated.
    
    Returns:
    str: Translated plain text
    """
    text = ""
    for part in morse.split(" "):     # Split morse code by space
        if part == "/":
            text += " "                # space in morse code indicates a space between words
        elif part in reverse_code:
            text += reverse_code[part]     # Map morse code to the corresponding character
        else:
            text += "?"      # Unknown morse code are represented by "?"
    return text

# Display options to the user
print("OPTION 1 : Translate English to Morse Code.")
print("OPTION 2 : Translate Morse Code into English")

# Get user choice
option = input("\nEnter an Option : ")

if option == "1":
    # Translate text to morse code
    text = input("Input Text : ").strip()     # Read and trim input text (that the input is clean and free from extra spaces that might affect on further process)
    morse_code = translate_to_morse(text)      # Call translated function
    print(morse_code)      # Output morse code

elif option == "2":
    # Translate morse code to text
    morse = input("Enter morse code : ").strip()    # Read and trim input Morse code (that the input is clean and free from extra spaces that might affect on further process)
    english_text = translate_to_text(morse)     # Call translated function
    print(english_text)    # Output translated text

else:
    # Handle invalid options
    print("Invalid Option. Please choose 1 or 2.")