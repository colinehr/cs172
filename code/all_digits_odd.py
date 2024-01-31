def all_digits_odd(num: str) -> bool:
    # User inputs a number
    # Tells us if every digit is odd or if at least one is even
    i = 0
    even = False
    while i < len(num):
        if int(num[i]) % 2 == 0:
            even = True
        i += 1
    if not even:
        return True
    else:
        return False


n = input("Give me a whole number: ")
while n != "":
    if all_digits_odd(n):
        print("All digits are odd!")
    else:
        print("At least one digit is even. :(")
    n = input("Give me a whole number: ")