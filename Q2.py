from PIL import Image

# Open the image
image_path = r'C:\Users\LENOVO\Desktop\OCR_image_to_text\1.PNG'
original_image = Image.open(image_path)

# Get the size of the image
width, height = original_image.size

# Generate the number
import time
current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

# Create a new image with converted pixels
new_image = Image.new('RGB', (width, height))

# Iterate through each pixel and apply the conversion
for x in range(width):
    for y in range(height):
        pixel_value = original_image.getpixel((x, y))
        if isinstance(pixel_value, int):
            r = g = b = pixel_value
        else:
            r, g, b = pixel_value[:3]  # Extract RGB values from RGBA or other formats

        r_new = min(r + generated_number, 255)
        g_new = min(g + generated_number, 255)
        b_new = min(b + generated_number, 255)
        new_image.putpixel((x, y), (r_new, g_new, b_new))

# Save the new image
new_image.save('chapter1out.png')

# Calculate the sum of red pixel values in the new image
red_sum = sum(r for r, _, _ in new_image.getdata())
print("Sum of red pixel values in the new image:", red_sum)


# Calculate the sum of red pixel values in the new image
red_sum = sum(r for r, _, _ in new_image.getdata())
print("Sum of red pixel values in the new image:", red_sum)

# Chapter 2: The Chamber of Strings

# Define the input string
input_string = '56aAw1984sktr235270aYmn145ss785fsq31D0'

# Separate numbers and letters
numbers = ''.join(c for c in input_string if c.isdigit())
letters = ''.join(c for c in input_string if c.isalpha())

# Convert even numbers to ASCII Code Decimal Values
even_numbers_ascii = [str(ord(c)) for c in numbers if int(c) % 2 == 0]

# Convert upper-case letters to ASCII Code Decimal values
upper_case_ascii = [str(ord(c)) for c in letters if c.isupper()]

print("Even numbers ASCII Code Decimal Values:", ', '.join(even_numbers_ascii))
print("Upper-case letters ASCII Code Decimal values:", ', '.join(upper_case_ascii))

# Cryptogram to decrypt
cryptogram = "\\VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

def decrypt(cryptogram, shift_key):
    decrypted_text = ''
    for char in cryptogram:
        if char.isalpha():
            # Shift the character by the shift_key value
            shifted_char = chr((ord(char.lower()) - ord('a') - shift_key) % 26 + ord('a'))
            decrypted_text += shifted_char.upper() if char.isupper() else shifted_char
        else:
            decrypted_text += char
    return decrypted_text

# Test decryption with shift_key values from 1 to 25
for shift_key in range(1, 26):
    decrypted_quote = decrypt(cryptogram, shift_key)
    print(f"Shift Key ({shift_key}): {decrypted_quote}")
