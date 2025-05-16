s = input().lower()
javob1 = 0
javob2 = 0
unlilar = "auioe"
undoshlar="qrtypsdfghjklzxcvbnm"
for harf in s:
    if harf in unlilar:
        javob1 += 1
for harf in s:
    if harf in undoshlar:
        javob2 += 1
print("unlilar:",javob1,"undoshlar",javob2)
