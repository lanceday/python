import random

num = random.randint(1,20)

input("Ask a question\n")

print("")

if num % 2 == 0 and num >= 1 and num <= 7:
    print("Very doubtful")
elif num % 2 == 1 and num >= 1 and num <= 7:
    print("No")
elif num % 2 == 0 and num >= 8 and num <= 13:
    print("Reply hazy, try again")
elif num % 2 == 1 and num >= 8 and num <= 13:
    print("Ask again later")
elif num % 2 == 0 and num >= 14 and num <= 20:
    print("Yes")
elif num % 2 == 1 and num >= 14 and num <= 20:
    print("Outlook good")

print("")