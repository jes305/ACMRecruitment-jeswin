num = -42
bits = 8

# Two's complement
binary = format(num & ((1 << bits) - 1), f'0{bits}b')

# Convert back to decimal
val = int(binary, 2)


print("Decimal:", num)
print("8-bit 2's complement:", binary)


