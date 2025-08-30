def caesar(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            base = 'A' if c.isupper() else 'a'
            result += chr((ord(c) - ord(base) + shift) % 26 + ord(base))
        else:
            result += c
    return result

# Example
msg = "ZHOFRPH"
shift = -3

enc = caesar(msg, shift)       # Encode
dec = caesar(enc, -shift)      # Decode

print("Original:", msg)
print("Encoded :", enc)
print("Decoded :", dec)
