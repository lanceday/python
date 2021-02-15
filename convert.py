# Python program to convert decimal number into binary, octal and hexadecimal number system
# Take decimal number from user
dec = int(input("Enter an integer: "))
print("\nThe decimal value of",dec,"is:\n")
print(format(dec,"08b"),"in binary.")
print(format(dec,"03o"),"in octal.")
print(format(dec,"02X"),"in hexadecimal.\n")