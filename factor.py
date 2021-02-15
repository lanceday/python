input_number = int(input("Enter A Number Please: "))
factors = []
for divisor in range(1, input_number+1):
        mod = input_number % divisor
        if mod == 0:
            factors.append(divisor)
print("\nFactors of %i are : " % input_number)
for element in factors:
        print(element, end=" ")
print("\n")