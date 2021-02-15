import struct

i=input("Enter hex sequence: ")

#Enter: 2a
#Enter: c3 b6
#Enter: e3 83 84
#Enter: f0 9f 90 8d

s=i.split(" ")
y=b""
for b in s: y+=bytes([int(b,16)])

dec = ord(y.decode('utf8'))

print("\nHex sequence: ",i)
print("Hex sequence (alt): ",i.replace(" ",""))
print("Decimal: ",dec)
byte_list = ['{:08b}'.format(b) for b in struct.pack('>L', dec)]
if int(byte_list[0]):
    print("Binary: ",byte_list[0]+" "+byte_list[1]+" "+byte_list[2]+" "+byte_list[3])
elif int(byte_list[1]):
    print("Binary: ",byte_list[1]+" "+byte_list[2]+" "+byte_list[3])
elif int(byte_list[2]):
    print("Binary: ",byte_list[2]+" "+byte_list[3])
else:
    print("Binary: ",byte_list[3])
print("Octal: ",format(dec,"03o"))
print("Hexadecimal: ",format(dec,"02X"))
print("UTF-8 value: ",(y))
print("Unicode character: ",chr(dec)+"\n")
