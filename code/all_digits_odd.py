# User inputs a number
# Tells us if every digit is odd or if at least one is even
num = input("Give me a whole number: ")
i = 0
even = False
zero = False
while i < len(num):
    if int(num[i]) % 2 == 0:
        even = True
    if int(num[i]) == 0:
        zero = True
    i += 1
if zero:
    print("There was a zero.")
elif not even:
    print("All digits are odd!")
else:
    print("Not all digits are odd. :(")