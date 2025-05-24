txt = input("txt: ")
cnt = 0
undered = []
for i in range(len(txt)):
    if cnt >= 2:
        if not txt[i] in undered and not txt[i] in 'aioeu' and i < len(txt)-1:
            print(txt[i], "_", sep="", end="")
            cnt = 0
            undered += [txt[i]]
            continue
    print(txt[i], end='')
    cnt += 1
