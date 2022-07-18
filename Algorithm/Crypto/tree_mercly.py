import hashlib


words = ["62af5c3cb8da3e4f25061e829ebeea5c7513c54949115b1acc225930a90154dad50c873877f38fcbc56dbe836b9d979912efcb587ed8eea919372d403b5c2bd4"]

hashes = [hashlib.sha256(str.encode(word)).hexdigest() for word in words]

for pair in zip(words, hashes):
    print(f"{pair[0]} : {pair[1]}")


# hash[0]   = 62af5c3cb8da3e4f25061e829ebeea5c7513c54949115b1acc225930a90154da
# hash[1]   = d50c873877f38fcbc56dbe836b9d979912efcb587ed8eea919372d403b5c2bd4
# hash[top] = 0bdf27bf7ec894ca7cadfe491ec1a3ece840f117989e8c5e9bd7086467bf6c38