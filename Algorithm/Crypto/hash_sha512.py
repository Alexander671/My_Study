import hashlib

words = ["Sky", "Grass", "Sun", "HelloHome", "привет", "Привет", "Blue"]

hashes = [hashlib.sha512(str.encode(word)).hexdigest() for word in words]

for pair in zip(words, hashes):
    print(f"{pair[0]} : {pair[1]}")


