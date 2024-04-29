def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key  # Reverse the shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char  # Non-alphabetical characters remain unchanged
    return decrypted_text

# Decrypt the encrypted code with the correct key
encrypted_code = "tybony_inevnoyr = 100\nzl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}\n\ndef cebprff_ahzoref():\n    global tybony_inevnoyr\n    ybpny_inevnoyr = 5\n    ahroref = []\n\n    while ybpny_inevnoyr > 0:\n        if ybpny_inevnoyr % 2 == 0:\n            ahroref.append(ybpny_inevnoyr)\n\n        ybpny_inevnoyr -= 1\n\n    return ahroref\n\nzl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}\nerfhyg = cebprff_ahzoref()\n\ndef zbqvsl_qvpg():\n    global tybony_inevnoyr\n    tybony_inevnoyr = 10\n\n    zl_qvpg['xrl4'] = tybony_inevnoyr\n\nzbqvsl_qvpg()\n\ndef hcqngr_tybony():\n    global tybony_inevnoyr\n    tybony_inevnoyr += 10\n\nfor i in range(5):\n    print(i)\n\nif 5 not in zl_frg and 'xrla' not in zl_qvpg and tybony_inevnoyr != 10:\n    print('Condition met!')\n\nprint(tybony_inevnoyr)\nprint(zl_qvpg)\nprint(zl_frg)\n"
key = 5  # The correct key value used for encryption

decrypted_code = decrypt(encrypted_code, key)
print("Decrypted Code:")
print(decrypted_code)

# Fixing errors and adding comments
tybony_inevnoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

def cebprff_ahzoref():
    global tybony_inevnoyr
    ybpny_inevnoyr = 5
    ahroref = []

    while ybpny_inevnoyr > 0:
        if ybpny_inevnoyr % 2 == 0:  # Check if number is even
            ahroref.append(ybpny_inevnoyr)  # Append even numbers to the list

        ybpny_inevnoyr -= 1  # Decrement ybpny_inevnoyr until it reaches 0

    return ahroref  # Return the list of even numbers

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref()  # Call the function to get the list of even numbers

def zbqvsl_qvpg():
    global tybony_inevnoyr
    tybony_inevnoyr = 10  # Set tybony_inevnoyr to 10

    zl_qvpg['xrl4'] = tybony_inevnoyr  # Add 'xrl4' to zl_qvpg with the value of tybony_inevnoyr

zbqvsl_qvpg()  # Call the function to update tybony_inevnoyr and zl_qvpg

def hcqngr_tybony():
    global tybony_inevnoyr
    tybony_inevnoyr += 10  # Increment tybony_inevnoyr by 10

for i in range(5):
    print(i)  # Print numbers from 0 to 4

if 5 not in zl_frg and 'xrla' not in zl_qvpg and tybony_inevnoyr != 10:
    print('Condition met!')  # Print 'Condition met!' if conditions are satisfied

print(tybony_inevnoyr)  # Print the value of tybony_inevnoyr
print(zl_qvpg)  # Print the dictionary zl_qvpg
print(zl_frg)  # Print the set zl_frg
