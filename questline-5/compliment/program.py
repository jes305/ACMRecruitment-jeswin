num = -42
bits = 8

# Two's complement
binary = format(num & ((1 << bits) - 1), f'0{bits}b')

# Convert back to decimal
val = int(binary, 2)
if binary[0] == '1':
    val -= (1 << bits)

print("Decimal:", num)
print("8-bit 2's complement:", binary)
print("Check back:", val)

