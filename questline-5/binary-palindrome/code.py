numbers=[9,12]
for num in numbers:
    b =bin(num)[2:]
    if b == b[::-1]:
        print (f"{num} in binary ({b}) palindrome")
    else:
        print(f"{num} in binary ({b}) not palindrome")
