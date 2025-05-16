text = input("Biror narsani yozing: ")
vowels = "aeiouAEIOU"
natija = ""

for i in text:
    if i in vowels:
        natija += "*"
    else:
        natija += i

print(natija)
