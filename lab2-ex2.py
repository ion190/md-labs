# Make a program that will implement the RSA algorithm made by you and with help of this program you can encrypt any string and then decrypt it.


# RSA ALGORITHM VARIABLES
p = 47
q = 79
n = p * q
nn = (p - 1) * (q - 1)
e = 7793
d = pow (e, -1, nn)

# Encryption
encrypt_input = input("enter the word(s) you want to encrypt:")
ascii_values = []
for char in encrypt_input:
    ascii_values.append(ord(char))
encrypt_output = [pow(val, e, n) for val in ascii_values]
print("Your encrypted Message:",encrypt_output)

# Decryption
decryption_step = input("Type yes if you want to decrypt the message back:")
if decryption_step in {"yes","ye","Ye","YE","Yes","YES"}:
    decrypt_output = [pow(val, d, n) for val in encrypt_output]
    decrypted_message = ''.join(chr(decrypted_val) for decrypted_val in decrypt_output)
    print("Your decrypted Message:",decrypted_message)
else:
    print("No decryption requested")

