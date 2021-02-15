# Python 3 code to demonstrate the  
# working of MD5 (string - hexadecimal) 
  
import hashlib
import base64 

# initializing string 
str2hash = input("Enter string to hash: ")

# then sending to md5() 
result = hashlib.md5(str2hash.encode()) 

sample_string_bytes = str2hash.encode("ascii") 
base64_bytes = base64.b64encode(sample_string_bytes) 
base64_string = base64_bytes.decode("ascii") 


# printing the equivalent hexadecimal value. 
print("\nThe string \'" + str2hash + "\' hashed is : \n", end ="")
print(f"\nBASE64: {base64_string}")
print("MD5: ", end ="")
print(result.hexdigest()) 
print("\n")
