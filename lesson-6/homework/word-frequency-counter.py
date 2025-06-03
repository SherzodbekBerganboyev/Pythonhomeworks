def chek():
    import string
    with open("sample.txt") as f:
        text = f.read()
        text = text.lower()
        for i in string.punctuation:
            text = text.replace(i, '')
        sozlar = text.split()
        tartib_sozlar = list(set(sozlar))
        for k in range(len(tartib_sozlar)):
            print(f"{tartib_sozlar[k]}-{sozlar.count(tartib_sozlar[k])} marta")
        return

chek()