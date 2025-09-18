sen = input("Enter the sentence: ")

words = sen.split()
freq = {}


for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

for word, count in items:
    print(f"{word} → {count}")

