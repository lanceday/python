import struct

Val = {range(10):range(48, 58), range(10,36): range(65, 91)}

def B2D(N,B1):
    '''From Base B1 to Decimal'''
    DN = 0
    for i in range(len(N)):
        for j in Val:
            if ord(N[i]) in Val[j]:
                FV=j[ord(N[i])-Val[j][0]]       # FaceValue of the Digit
        if FV>= B1:                             # Digits aren't >=Base, right?
            print("Base Error..")
            exit()
        else:
            DN += FV * (B1 ** (len(N) - 1 - i))
    return DN

def D2B(DN,B2):
    '''From Decimal to Base B2'''
    if int(DN) == 0:
        BN = '0'
    else:
        BN = ""
        while DN > 0:
            R = DN % B2
            for i in Val:
                if R in i:
                    BN+=chr(Val[i][R-i[0]])     #Finding the Digit for the Value
            DN = int(DN / B2)
    return BN[::-1]

def B2B(N,B1,B2):
    return D2B(B2D(N,B1),B2)

N=input("\nNum: ").upper()
B1=int(input("FromBase: "))
B2=int(B2D(N,B1))

print("\nBase Conversions:")
print(format(B2D(N,B1)),"in decimal.")
byte_list = ['{:08b}'.format(b) for b in struct.pack('>L', B2D(N,B1))]
if int(byte_list[0]):
    print(byte_list[0]+" "+byte_list[1]+" "+byte_list[2]+" "+byte_list[3],"in binary.")
elif int(byte_list[1]):
    print(byte_list[1]+" "+byte_list[2]+" "+byte_list[3],"in binary.")
elif int(byte_list[2]):
    print(byte_list[2]+" "+byte_list[3],"in binary.")
else:
    print(byte_list[3],"in binary.")
print(format(B2D(N,B1),"03o"),"in octal.")
print(format(B2D(N,B1),"02X"),"in hexadecimal.")
if B2D(N,B1) < 1114112:
    print(chr(B2D(N,B1)),"is the character value.\n")
else:
    print("Character unavailable.\n")