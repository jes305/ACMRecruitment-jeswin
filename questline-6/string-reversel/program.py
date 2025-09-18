
def reverse_iterative(s):
    rev = ""
    for ch in s:
        rev = ch + rev   
    return rev

def reverse_recursive(s):
    return s if len(s) <= 1 else reverse_recursive(s[1:]) + s[0]


s = input("Enter a string: ")
print("Iterative Reverse:", reverse_iterative(s))
print("Recursive Reverse:", reverse_recursive(s))

